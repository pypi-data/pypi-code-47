import asyncio
from concurrent import futures
import errno
import logging
import uuid

from ..core import BaseClient, LoopHelper
from .external_task_handler import ExternalTaskHandler

logger = logging.getLogger(__name__)

class ExternalTaskClient(BaseClient):

    def __init__(self, url, session=None, identity=None):
        super(ExternalTaskClient, self).__init__(url, session, identity)

        self.__loop_helper = LoopHelper(on_shutdown=self.__on_shutdown)
        self.__worker_id = str(uuid.uuid4())

        self._topic_for_worker = {}

    def subscribe_to_external_task_for_topic(self, topic, worker):
        if topic in self._topic_for_worker:
            logger.warning(f"The topic '{topic}' skipped, is already registered.'")
        else:
            self.__start_subscription(topic, worker)

    def __start_subscription(self, topic, worker):
        async def bg_job_handle_external_tasks():
            try:
                await self.handle_external_tasks(topic, worker)
            except Exception as e:
                if type(e) is errno.EPIPE:
                    logger.info(f"exception on handle_external_task: {e}")                    
                else:
                    logger.warn(f"exception on handle_external_task: {e}")

        async_bg_task = self.__loop_helper.register_background_task(bg_job_handle_external_tasks)
        self._topic_for_worker[topic] = async_bg_task

    def subscribe_to_external_tasks_for_topics(self, topics_for_workers):
        for topic in topics_for_workers.keys():
            worker = topics_for_workers[topic]

            self.subscribe_to_external_task_for_topic(topic, worker)

    def start(self):
        logger.info(f"Starting external task for topics {self._topic_for_worker.keys()}")
        self.__loop_helper.start()

    async def handle_external_tasks(self, topic, worker):
        external_tasks = await self.__fetch_and_lock(topic, worker)

        len_external_tasks = len(external_tasks)
        if len_external_tasks >= 1:
            logger.info(f"receive {len_external_tasks} tasks for topic '{topic}'.")


            def start_task(worker, external_task):
                external_task_handler = ExternalTaskHandler(
                    self._url, 
                    self._session, 
                    self._identity, 
                    self.__loop_helper,
                    worker, 
                    external_task)
                return external_task_handler.start()

            external_task_tasks = []

            for external_task in external_tasks:
                task = start_task(worker, external_task)
                external_task_tasks.append(task)

            try:
                done_tasks, pending = await asyncio.wait(external_task_tasks, return_when=futures.ALL_COMPLETED)
            except Exception as e:
                logger.error(f"asyncio.wait({e} - {type(e)})")

    async def __on_shutdown(self):
        await self.close()

    def stop(self):
        logger.info(f"Stopping external task for topics {self._topic_for_worker.keys()}")
        self.__loop_helper.stop()

    async def __fetch_and_lock(self, topic, worker, options={}):
        logger.debug(f"fetch and lock external task for topic {topic}")

        max_tasks = options.get('max_tasks', 10)
        long_polling_timeout = options.get('long_polling_timeout', 10_000)
        lock_duration = options.get('lock_duration', 30_000)

        request = {
            "workerId": self.__worker_id,
            "topicName": topic,
            "maxTasks": max_tasks,
            "longPollingTimeout": long_polling_timeout,
            "lockDuration": lock_duration
        }

        external_tasks = await self.do_post('/api/external_task/v1/fetch_and_lock', request)

        logger.debug(f"receive {len(external_tasks)} for topic {topic}.")

        return external_tasks
