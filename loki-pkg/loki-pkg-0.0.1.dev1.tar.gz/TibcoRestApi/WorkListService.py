import requests, os , json, urllib
from requests.auth import HTTPBasicAuth
from loki import Config


class WorkListService(object):

    def __init__(self):
        try:
            self.parameters = Config()
            self.headers = {"Content-Type":"application/json",
                            "Accept":"application/json"}

            self.baseurl = self.parameters.config.get('SERVER', 'baseurl')
            self.base64auth = HTTPBasicAuth(self.parameters.config.get('AUTH','user'), self.parameters.config.get('AUTH','pwd'))
        
        except Exception as ex:
            print ex

    def getWorkListItems(self, _entitytype, _entityguid, _start=0, _count=50):
        try:
            endpoint = self.parameters.config.get('ENDPOINTS', 'getWorkListItems').format(entitytype=_entitytype, entityguid=_entityguid, start=_start, count=_count)
            request_url = "{baseurl}{endpoint}".format(baseurl=self.baseurl, endpoint=endpoint)

            request_response = requests.request("GET", request_url, headers=self.headers, auth=self.base64auth)

            return json.loads(request_response.content)

        except Exception as ex:
            print ex
    
    def getWorkListItemsAllResources(self, _start=0, _count=50):
        try:
            endpoint = self.parameters.config.get('ENDPOINTS', 'getWorkListItemsAllResources').format(start=_start, count=_count)
            request_url = "{baseurl}{endpoint}".format(baseurl=self.baseurl, endpoint=endpoint)

            request_response = requests.request("GET", request_url, headers=self.headers, auth=self.base64auth)

            return json.loads(request_response.content)
        
        except Exception as ex:
            print ex

''' 
import requests

url = "http://localhost:8080/bpm/rest/worklist/itemsall/{{resourcetype}}/{{start}}/{{count}}"
z
payload = {}
headers = {
  'Authorization': 'Basic dGliY28tYWRtaW46c2VjcmV0',
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
print(response.text.encode('utf8'))
'''