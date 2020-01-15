import mock
import json
from django.test import TestCase
from django.test.client import RequestFactory
from stripe.error import StripeError
from zebra.views import verify_stripe_event, webhooks_v2


TEST_EVENT_NAME = 'zebra webhook whatever'
TEST_EVENT_ID = 'test id'


class WebhooksV2Tests(TestCase):
    def setUp(self):
        patcher = mock.patch('zebra.views.WEBHOOK_MAP')
        self.mock_webhook_map = patcher.start()
        self.mock_webhook_map.__contains__.return_value = True
        self.addCleanup(patcher.stop)

        patcher = mock.patch('zebra.views.verify_stripe_event')
        self.mock_verify = patcher.start()
        self.addCleanup(patcher.stop)

        self.request = RequestFactory().post('/some/url/')
        self.event_name = "plan.created"
        self.event_key = self.event_name.replace('.', '_')
        self.event_data = {'type': self.event_name}
        self.request._body = json.dumps(self.event_data)

    def test_known_signal_send_is_called(self):
        webhooks_v2(self.request)
        webhook_get = self.mock_webhook_map.__getitem__
        webhook_get.assert_called_once_with(self.event_key)
        signal = webhook_get.return_value
        signal.send.assert_called_once_with(full_json=self.event_data,
                                            sender=None)

    def test_known_signal_verify_stripe_event_is_called(self):
        webhooks_v2(self.request)
        self.mock_verify.assert_called_once_with(self.event_key,
                                                 self.event_data)

    def test_unknown_signal_name_then_no_signal_is_sent(self):
        self.mock_webhook_map.__contains__.return_value = False
        webhooks_v2(self.request)
        self.assertEqual(self.mock_webhook_map.__getitem__.call_count, 0)

    def test_unknown_signal_verify_stripe_event_not_called(self):
        self.mock_webhook_map.__contains__.return_value = False
        webhooks_v2(self.request)
        self.assertEqual(self.mock_verify.call_count, 0)


class VerifyStripeEventTests(TestCase):
    def setUp(self):
        patcher = mock.patch('zebra.views.WEBHOOK_MAP')
        self.mock_webhook_map = patcher.start()
        self.addCleanup(patcher.stop)

        patcher = mock.patch('zebra.views.stripe.Event')
        self.mock_event = patcher.start()
        self.addCleanup(patcher.stop)
        self.test_json = {'id': TEST_EVENT_ID}

    def test_stripe_event_retrieve_is_called(self):
        verify_stripe_event(TEST_EVENT_NAME, self.test_json)
        self.mock_event.retrieve.assert_called_once_with(TEST_EVENT_ID)

    def test_verified_signal_send_is_called(self):
        verify_stripe_event(TEST_EVENT_NAME, self.test_json)
        webhook_get = self.mock_webhook_map.__getitem__
        webhook_get.assert_called_once_with(TEST_EVENT_NAME+"_verified")
        signal = webhook_get.return_value
        event_data = self.mock_event.retrieve.return_value.to_dict.return_value
        signal.send.assert_called_once_with(full_json=event_data, sender=None)

    def test_verified_signal_not_sent_if_stripe_event_retrieve_fails(self):
        self.mock_event.retrieve.side_effect = StripeError
        verify_stripe_event(TEST_EVENT_NAME, self.test_json)
        signal = self.mock_webhook_map.__getitem__.return_value
        self.assertEqual(signal.send.call_count, 0)
