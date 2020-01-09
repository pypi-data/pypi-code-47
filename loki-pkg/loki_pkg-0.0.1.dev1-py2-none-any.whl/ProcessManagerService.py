import requests, os , json, urllib
from requests.auth import HTTPBasicAuth
from loki import Config

class ProcessManagerService(object):

    def __init__(self):
        try:
            self.parameters = Config()
            self.headers = {"Content-Type":"application/json",
                            "Accept":"application/json"}

            self.baseurl = self.parameters.config.get('SERVER', 'baseurl')
            self.base64auth = HTTPBasicAuth(self.parameters.config.get('AUTH','user'), self.parameters.config.get('AUTH','pwd'))
        
        except Exception as ex:
            print ex

    def listServices(self):
        try:
            endpoint = self.parameters.config.get('ENDPOINTS', 'listServices')
            request_url = "{baseurl}{endpoint}".format(baseurl=self.baseurl, endpoint=endpoint)

            request_response = requests.request("GET", request_url, headers=self.headers, auth=self.base64auth)

            return json.loads(request_response.content)


        except Exception as ex:
            print ex

    def startProcessIncomingReceiveTask(self, _modulename, _processname, _version, _payload):
        try:
            self.headers["Content-Type"] = "application/xml"
            self.headers["Accept"] = "application/xml"
            query_param = {"responsetype":"XML"}

            _encoded_modulename = urllib.quote(_modulename, safe='')
            endpoint = self.parameters.config.get('ENDPOINTS', 'startProcessIncomingReceiveTask').format(modulename=_encoded_modulename, processname=_processname, version=_version)
            request_url = "{baseurl}{endpoint}".format(baseurl=self.baseurl, endpoint=endpoint)

            request_response = requests.request("POST", request_url, headers=self.headers, data = _payload, params=query_param)

            return request_response.content

        except Exception as ex:
            print ex