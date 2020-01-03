import json
import datetime
import requests
from loguru import logger
from pipelinevilma.Messager import Messager


class CollectorDataApi:
    STATUS_FOR_LABELING = 'labeling-required'

    def __init__(self, data_api):
        self.base_url = str(data_api['base_url']) + ":" + str(data_api['port']) + "/"
        self.include_task_endpoint = str(data_api['endpoints']['include_task'])
        logger.debug(f"base_url: {self.base_url}")
        logger.debug(f"include_task_endpoint: {self.include_task_endpoint}")

    def _add_collector_properties(self, message):
        message['createdAt'] = int(datetime.datetime.utcnow().strftime("%s"))
        message['status'] = CollectorDataApi.STATUS_FOR_LABELING
        logger.debug(message)
        return message

    def _include_task(self, message):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = message
        url = self.base_url + self.include_task_endpoint
        logger.debug(f"URL: {url}")
        logger.debug(f"Data: {data}")
        res = requests.post(url, data=json.dumps(data), headers=headers)
        
        if not res:
            return False
        return res

    def store(self, message):
        # Include API data
        message = self._add_collector_properties(message)
        response = self._include_task(message)

        if not response:
            return False

        if response.status_code == 200:
            return True

        return False


# if __name__ == "__main__":
#     data_api = {
#         "base_url": "http://localhost",
#         "port": "3333",
#         "endpoints": {
#             "include_task": "collector"
#         }
#     }
#     message = {
#         "x": {
#             "sensorId": 1,
#             "metaType": "tests",
#             "description": "tests from CollectorDataApi",
#             "url": "",
#             "dataType": "test",
#             "data": "test Data",
#         },
#         "y": {
#             "true": [],
#             "pred": [],
#         }
#     }

#     api = CollectorDataApi(data_api)
#     api.store(message)
