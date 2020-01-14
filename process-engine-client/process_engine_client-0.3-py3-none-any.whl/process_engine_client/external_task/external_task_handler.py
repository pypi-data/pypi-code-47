import asyncio
import inspect
import logging

from ..core import BaseClient, LoopHelper

logger = logging.getLogger(__name__)

class ExternalTaskHandler(BaseClient):
    
    def __init__(self, url, session, identity, loop_helper, worker, external_task, options={}):
        super(ExternalTaskHandler, self).__init__(url, session, identity)
        self._loop_helper = loop_helper
        self._worker = worker
        self._worker_spec = inspect.getfullargspec(self._worker)
        self._external_task = external_task
        self._payload = self._external_task['payload']
        self._options = options
        self._async_extend_lock = None
        self._async_run_worker = None

    async def start(self):
        try:
            result = None
            
            if asyncio.iscoroutinefunction(self._worker):
                if len(self._worker_spec.args) == 2:
                    result = await self._worker(self._payload, self._external_task)
                else:
                    result = await self._worker(self._payload)
            else:
                if len(self._worker_spec.args) == 2:
                    result = self._worker(self._payload, self._external_task)
                else:
                    result = self._worker(self._payload)

            await self.__finish_task_successfully(result)

        except Exception as e:
            # TODO: log message for unhandled error
            await self.__finish_task_with_technical_errors(str(e), str(e))

    def _stop_async_extend_lock(self):
        if self._async_extend_lock:
            try:
                self._async_extend_lock.cancel()
            except asyncio.CancelledError:
                pass
            self._async_extend_lock = None

    async def extend_lock(self, worker_id, external_task_id, additional_duration):
        url = f"/api/external_task/v1/task/{external_task_id}/extend_lock"

        request = {
            "workerId": worker_id,
            "additionalDuration": additional_duration
        }

        await self.do_post(url, request)

    async def __finish_task_successfully(self, result):
        logger.info(f"finish task {self._external_task['id']} successfully.")
        path = f"/api/external_task/v1/task/{self._external_task['id']}/finish"

        payload = {
            "workerId": self._external_task['workerId'],
            "result": result
        }

        result = await self.do_post(path, payload)
        logger.debug(f"finished task {self._external_task['id']} successfully.")

    async def __finish_task_with_functional_errors(self, error_code, error_message):
        logger.warn(f"finished external task_with functional errors '{self._external_task}', '{error_code}', '{error_message}'.")

        path = f"/api/external_task/v1/task/{self._external_task['id']}/handle_bpmn_error"

        payload = {
            "workerId": self._external_task['workerId'],
            "errorCode": error_code,
            "errorMessage": error_message
        }

        await self.do_post(path, payload)

    async def __finish_task_with_technical_errors(self, error_message, error_details):
        logger.warn(f"finished task with technical errors '{self._external_task}', '{error_message}', '{error_details}'.")

        path = f"/api/external_task/v1/task/{self._external_task['id']}/handle_service_error"

        payload = {
            "workerId": self._external_task['workerId'],
            "errorMessage": error_message,
            "errorDetails": error_details
        }

        await self.do_post(path, payload)