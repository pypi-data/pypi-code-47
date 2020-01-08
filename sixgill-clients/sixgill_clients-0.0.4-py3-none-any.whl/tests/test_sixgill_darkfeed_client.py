from mock import patch
import logging
import json

from sixgill.sixgill_darkfeed_client import SixgillDarkFeedClient
from tests.test_sixgill_base_client import TestSixgillBaseClient


class TestSixgillDarkFeedClient(TestSixgillBaseClient):

    def setUp(self) -> None:
        super(TestSixgillDarkFeedClient, self).setUp()
        self.sixgill_darkfeed_client = SixgillDarkFeedClient('client_id', 'secret', 'random', logging.getLogger("test"))

    def test_get_incidents(self):
        with patch('requests.sessions.Session.send', new=self.mocked_request):
            incidents = []
            for incident in self.sixgill_darkfeed_client.get_incidents():
                self.sixgill_darkfeed_client.mark_digested_item(incident)
                incidents.append(incident)

        expected_output = [{'consumer_specific_info': {'content': 'some data #1'},
                            'id': '5dd897f59dfc16000180c0d0'},
                           {'consumer_specific_info': {'content': 'some data #2'},
                            'id': '5dd897f59dfc16000180c0d1'},
                           {'consumer_specific_info': {'content': 'some data #3'},
                            'id': '5dd897f59dfc16000180c0d2'},
                           {'consumer_specific_info': {'content': 'some data #4'},
                            'id': '5dd897f59dfc16000180c0d3'},
                           {'consumer_specific_info': {'content': 'some data #5'},
                            'id': '5dd897f59dfc16000180c0d4'},
                           {'consumer_specific_info': {'content': 'some data #6'},
                            'id': '5dd897f59dfc16000180c0d5'}]

        self.assertEqual(incidents, expected_output)

    def test_mark_and_submit(self):
        with patch('requests.sessions.Session.send', new=self.mocked_request):
            incidents = json.loads(self.mocked_incidents_response)

            for incident in incidents:
                self.sixgill_darkfeed_client.mark_digested_item(incident)

            expected_output = ['5dd897f59dfc16000180c0d0',
                               '5dd897f59dfc16000180c0d1',
                               '5dd897f59dfc16000180c0d2',
                               '5dd897f59dfc16000180c0d3',
                               '5dd897f59dfc16000180c0d4',
                               '5dd897f59dfc16000180c0d5']

            self.assertEqual(self.sixgill_darkfeed_client.digested_ids, expected_output)

            self.sixgill_darkfeed_client.submit_digested_items(force=True)

            self.assertEqual(self.sixgill_darkfeed_client.digested_ids, [])