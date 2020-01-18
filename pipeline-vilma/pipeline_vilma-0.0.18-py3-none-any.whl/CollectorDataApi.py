import json
import datetime
import requests
from loguru import logger
from pipelinevilma.Messager import Messager


class CollectorDataApi:
    STATUS_FOR_LABELING = 'labeling-required'

    def __init__(self, storage_api):
        self.base_url = str(storage_api['base_url']) + ":" + str(storage_api['port']) + "/"
        self.add_item_endpoint = str(storage_api['endpoints']['add_item'])
        logger.debug(f"base_url: {self.base_url}")
        logger.debug(f"add_item_endpoint: {self.add_item_endpoint}")

    def _add_labeling_properties(self, message):
        message['createdAt'] = int(datetime.datetime.utcnow().strftime("%s"))
        message['status'] = CollectorDataApi.STATUS_FOR_LABELING
        return message

    def _insert_on_db(self, message):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        url = self.base_url + self.add_item_endpoint
        logger.debug(f"URL: {url}")
        res = requests.post(url, data=json.dumps(message), headers=headers)

        if not res:
            return False
        return res

    def store(self, message):
        # Include API data
        message = self._add_labeling_properties(message)
        api_response = self._insert_on_db(message)

        if not api_response:
            return False

        if api_response.status_code == 200:
            return True

        return False
