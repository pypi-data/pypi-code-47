import requests, os , json, urllib
from requests.auth import HTTPBasicAuth
from loki import Config


class WorkItemManagementService(object):

    def __init__(self):

        try:
            self.parameters = Config()
            self.headers = {"Content-Type":"application/json",
                            "Accept":"application/json"}

            self.baseurl = self.parameters.config.get('SERVER', 'baseurl')
            self.base64auth = HTTPBasicAuth(self.parameters.config.get('AUTH','user'), self.parameters.config.get('AUTH','pwd'))
        
        except Exception as ex:
            print ex

    def completeWorkItem(self, _id, _userid, _typeuid, _typeversion, _payload):
        try:
            self.headers["Content-Type"] = "application/xml"

            endpoint = self.parameters.config.get('ENDPOINTS', 'completeWorkItem').format(id=_id,userid=_userid, typeuid=_typeuid, typeversion=_typeversion)
            request_url = "{baseurl}{endpoint}".format(baseurl=self.baseurl, endpoint=endpoint)

            request_response = requests.request("PUT", request_url, headers=self.headers, data = _payload, auth=self.base64auth)

            return request_response.content

        except Exception as ex:
            print ex

    def allocate_open_wi(self, workitemid, workitemversion, resource):

        try:
        
            endpoint = self.parameters.config.get('ENDPOINTS', 'allocateAndOpenWorkItem')

            request_url = "{baseurl}{endpoint}".format(baseurl=self.baseurl, endpoint=endpoint)
            querystring = {"id":int(workitemid),"version":int(workitemversion),"resources":resource}

            request_response = requests.request("PUT", request_url, headers=self.headers, params=querystring, auth=self.base64auth)

            return json.loads(request_response.content)
        except Exception as ex:
            print ex

