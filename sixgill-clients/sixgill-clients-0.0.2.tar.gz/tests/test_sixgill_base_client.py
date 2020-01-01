from unittest import TestCase
from mock import patch
import logging
import json

from sixgill.sixgill_base_client import SixgillBaseClient


class MockedResponse(object):
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text

    def json(self):
        return json.loads(self.text)


class TestSixgillBaseClient(TestCase):

    def setUp(self) -> None:
        self.sixgill_client = SixgillBaseClient('client_id', 'secret', 'random', logging.getLogger("test"))
        self.mocked_incidents_response = mocked_incidents_response
        self.mocked_get_token_response = mocked_get_token_response
        self.mocked_alerts_response = mocked_alerts_response
        self.mocked_put_response = mocked_put_response
        self.mocked_patch_response = mocked_patch_response

    def mocked_request(self, *args, **kwargs) -> MockedResponse:
        request = kwargs.get("request", {})
        end_point = request.path_url
        method = request.method

        if (method == 'PUT' or method == 'PATCH') and request.body:
            self.mocked_incidents_response = '''[]'''
            self.mocked_alerts_response = '''[]'''

        self.response_dict = {
            'POST': {
                '/auth/token':
                    MockedResponse(200, self.mocked_get_token_response),
            },
            'GET': {
                '/alerts/feed?consumer=random&include_delivered_items=False&limit=1000&skip=0':
                    MockedResponse(200, self.mocked_incidents_response),
                '/alerts/actionable-alert?sort_order=asc&is_read=unread&fetch_size=1000&offset=0':
                    MockedResponse(200, json.dumps(json.loads(self.mocked_alerts_response)))
            },
            'PUT': {
                '/alerts/feed?consumer=random': MockedResponse(200, self.mocked_put_response)
            },
            'PATCH': {
                '/alerts/actionable-alert': MockedResponse(200, self.mocked_patch_response)
            }
        }
        response_dict = self.response_dict.get(method)
        return response_dict.get(end_point)

    def test_get_access_token(self):
        with patch('requests.sessions.Session.send', new=self.mocked_request):
            access_token = self.sixgill_client._get_access_token()

        expected_output = "this_is_my_token"
        self.assertEqual(access_token, expected_output)


mocked_get_token_response = '''{"access_token": "this_is_my_token"}'''
mocked_put_response = '''{"status": 200, "message": "Successfully Marked as Ingested Feed Items"}'''
mocked_patch_response = '''{"status": 200, "message": "Successfully updated Actionable Alerts"}'''
mocked_incidents_response = '''[
  {
    "consumer_specific_info": {
      "content": "some data #1"
    },
    "id": "5dd897f59dfc16000180c0d0"
  },
  {
    "consumer_specific_info": {
      "content": "some data #2"
    },
    "id": "5dd897f59dfc16000180c0d1"
  },
  {
    "consumer_specific_info": {
      "content": "some data #3"
    },
    "id": "5dd897f59dfc16000180c0d2"
  },
  {
    "consumer_specific_info": {
      "content": "some data #4"
    },
    "id": "5dd897f59dfc16000180c0d3"
  },
  {
    "consumer_specific_info": {
      "content": "some data #5"
    },
    "id": "5dd897f59dfc16000180c0d4"
  },
  {
    "consumer_specific_info": {
      "content": "some data #6"
    },
    "id": "5dd897f59dfc16000180c0d5"
  }
]'''


mocked_alerts_response = '''[
    {
        "alert_name": "someSecretAlert2",
        "content": "",
        "date": "2019-08-06 23:20:35", 
        "id": "1", 
        "lang": "English", 
        "langcode": "en",
        "read": false, 
        "severity": 10, 
        "threat_level": "emerging", 
        "threats": ["Phishing"],
        "title": "someSecretAlert2", 
        "user_id": "123"},
    {
        "alert_name": "someSecretAlert4",
        "content": "",
        "date": "2019-08-18 09:58:10", 
        "id": "2", 
        "read": false, 
        "severity": 10,
        "threat_level": "imminent", 
        "threats": ["Data Leak", "Phishing"], 
        "title": "someSecretAlert4",
        "user_id": "132"}, 
    {
        "alert_name": "someSecretAlert1",
         "content": "",
         "date": "2019-08-18 22:58:23",
         "id": "3", 
         "read": false,
         "severity": 10, 
         "threat_level": "imminent",
         "threats": ["Data Leak", "Phishing"],
         "title": "someSecretAlert1",
         "user_id": "123"},
    {
        "alert_name": "someSecretAlert2",
        "content": "",
        "date": "2019-08-19 19:27:24", 
        "id": "4", 
        "lang": "English", 
        "langcode": "en",
        "read": false, 
        "severity": 10, 
        "threat_level": "emerging", 
        "threats": ["Phishing"],
        "title": "someSecretAlert2", 
        "user_id": "123"},
    {
        "alert_name": "someSecretAlert3",
        "content": "",
        "date": "2019-08-22 08:27:19",
        "id": "5", 
        "read": false, 
        "severity": 10,
        "threat_level": "imminent", 
        "threats": ["Data Leak", "Phishing"], 
        "title": "someSecretAlert3",
        "user_id": "123"}, 
    {
        "alert_name": "someSecretAlert1",
        "content": "",
        "date": "2019-08-22 08:43:15",
        "id": "6", 
        "read": false,
        "severity": 10, 
        "threat_level": "imminent",
        "threats": ["Data Leak", "Phishing"],
        "title": "someSecretAlert1",
        "user_id": "123"
    }]'''