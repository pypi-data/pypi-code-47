import requests, pprint
from soco_parser.config import Config
from soco_parser.cloud import CloudBucket

class DocAPI(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.cloud = CloudBucket()

    def _get_header(self):
        return {'Content-Type': 'application/json', "Authorization": self.api_key}

    def parse_url(self, file_url):
        body = {"file_url":file_url,"file_type":"url","client_id":"soco_parser"}
        result = requests.post(url=Config.URL, headers= self._get_header(), json=body)
        if result.status_code >= 300:
            print("Error in connecting to the SOCO servers")
            return None
        return result.json()["data"]

    def parse_local_file(self, file_name):
        file = self.cloud.upload(file_name)
        if file:
            body = {"file_url": file, "file_type": "s3", "client_id": "soco_parser"}
            result = requests.post(url=Config.URL, headers=self._get_header(), json=body)
            if result.status_code >= 300:
                print("Error in connecting to the SOCO servers")
                return None
            return result.json()["data"]
        else:
            return None

