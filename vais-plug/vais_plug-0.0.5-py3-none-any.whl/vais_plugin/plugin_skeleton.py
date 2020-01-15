from abc import abstractmethod
import os
import requests
import json
import logging
from rq import Worker, Queue
from redis import Redis
import traceback
from rq.job import Job, JobStatus
import time


class PluginSkeleton(object):
    redis = None
    FAILED = "failed"
    SUCCESS = "success"

    def __init__(self):
        os.environ['PLUGIN_CODE'] = "{}/{}".format(os.environ.get('PLUGIN_CODE'), self.plugin_version_name())
        os.environ['JOB_QUEUE'] = "{}/{}".format(os.environ.get('JOB_QUEUE'), self.plugin_version_name())
        logging.info("Init connection to redis {}:{}".format(os.environ.get('REDIS_HOST'),
                                                             os.environ.get('REDIS_PORT')))
        PluginSkeleton.redis = Redis(host=os.environ.get('REDIS_HOST'),
                                     port=os.environ.get('REDIS_PORT'))
        logging.info("Redis info: {}".format(PluginSkeleton.redis.info()))

    @abstractmethod
    def preload(self):
        pass

    @abstractmethod
    def plugin_version_name(self):
        return "normal"

    @staticmethod
    def registry_plugin(file_exec, func_exec, version_code, version_name):
        assert version_name is not None, "version_name none is not accepted"
        try:
            payload = {
                "description": os.environ.get('PLUGIN_DESCRIPTION'),
                "job_queue_name": os.environ.get('JOB_QUEUE'),
                "function_name": "{}.{}".format(file_exec[file_exec.rindex(os.sep) + 1:file_exec.rindex('.')],
                                                func_exec.__name__),
                "plugin_name": os.environ.get('PLUGIN_NAME'),
                "plugin_code": os.environ.get('PLUGIN_CODE'),
                "depended_plugin_code": os.environ.get('DEPENDED_PLUGIN_CODE'),
                "plugin_version_code": version_code,
            }
            headers = {
                'Content-Type': "application/json"
            }
            logging.info("Resister worker: {}".format(json.dumps(payload)))
            response = requests.request("POST", os.environ.get('BACKEND_ENDPOINT'), data=json.dumps(payload),
                                        headers=headers, timeout=10)

            return response.status_code
        except:
            return 500

    @staticmethod
    def handler_error(job, exc_type, exc_value, traceback_):
        job_id = job.id
        job_index = job.args[0]
        description_error = " ".join(traceback.format_exception(exc_type, exc_value, traceback_))
        logging.info(job, traceback)
        PluginSkeleton.push_job_status(job_id, job_index, PluginSkeleton.FAILED, description=description_error)

    def run(self, file_exec, func_exec, version_code, ignore_register=False):
        # register plugin
        register_status = self.registry_plugin(file_exec, func_exec, version_code, self.plugin_version_name())
        if register_status == 201 or ignore_register:
            logging.info('Plugin {} Resisted'.format(os.environ.get('PLUGIN_NAME')))
            self.preload()
            queue = Queue(name=os.environ.get('JOB_QUEUE'), connection=PluginSkeleton.redis)
            # Start a worker with a custom name
            worker = Worker([queue], connection=PluginSkeleton.redis, exception_handlers=[PluginSkeleton.handler_error])
            worker.work(logging_level="INFO")
        else:
            logging.error('Plugin {} register failed'.format(os.environ.get('PLUGIN_NAME')))

    @staticmethod
    def push_job_status(doc_id, doc_index, result, description=None):
        output = {
            "id": doc_id,
            "index": doc_index + "_log",
            "status": result,
            "end_process_time": time.time(),
            "traceback": description
        }
        return PluginSkeleton.redis.lpush('result', json.dumps(output))

    @staticmethod
    def push_start_time_process(doc_id, doc_index):
        output = {
            "id": doc_id,
            "index": doc_index + "_log",
            "start_process_time": time.time()
        }
        return PluginSkeleton.redis.lpush('result', json.dumps(output))

    @staticmethod
    def push_result(doc_index, doc_id, result, version_code):
        output = {
            "id": doc_id,
            "index": doc_index,
            os.environ.get('PLUGIN_CODE'): {
                "version_code": version_code,
                "update_time": time.time(),
                "plugin_code": os.environ.get('PLUGIN_CODE')[:os.environ.get('PLUGIN_CODE').index('/')] if
                '/' in os.environ.get('PLUGIN_CODE') else os.environ.get('PLUGIN_CODE'),
                "data": result
            }
        }
        return PluginSkeleton.redis.lpush('result', json.dumps(output))

    @staticmethod
    def get_output_result(result, version_code):
        output = {
            os.environ.get('PLUGIN_CODE'): {
                "version_code": version_code,
                "data": result
            }
        }
        return output

    @staticmethod
    def get_depended_jobs_output(current_job, input_data, depended_jobs=None):
        """
        :param input_data:
        :param current_job:
        :param depended_jobs: {
            "plugin_code": "job_id",
            "plugin_code": "job_id",
                ...
        }
        :return:
        """

        previous_job = current_job.dependency
        if previous_job:
            results = {}
            # append input_data with depended on job result
            for item in previous_job.result.items():
                results[item[0][:item[0].index('/')]] = item[1]
            PluginSkeleton.push_start_time_process(current_job.get_id(), current_job.args[0])
            return results
        elif depended_jobs:
            jobs = {item[0]: Job.fetch(item[1], connection=PluginSkeleton.redis) for item in depended_jobs.items()}
            while True:
                jobs_status = [item.get_status() for item in jobs.values()]
                count_jobs_failed = jobs_status.count(JobStatus.FAILED)
                if count_jobs_failed > 0:
                    PluginSkeleton.push_start_time_process(current_job.get_id(), current_job.args[0])
                    return None
                count_jobs_finish = jobs_status.count(JobStatus.FINISHED)
                if count_jobs_finish == len(jobs):
                    results = {item[0][:item[0].index('/')]: item[1].result[item[0]] for item in jobs.items()}
                    if input_data:
                        # append input_data with depended on job result
                        for item in input_data.items():
                            if not results.get(item[0]):
                                results[item[0][:item[0].index('/')]] = item[1]
                    PluginSkeleton.push_start_time_process(current_job.get_id(), current_job.args[0])
                    return results
                time.sleep(0.1)
        else:
            results = {}
            # append input_data with depended on job result
            for item in input_data.items():
                results[item[0][:item[0].index('/')]] = item[1]

            PluginSkeleton.push_start_time_process(current_job.get_id(), current_job.args[0])
            return results
