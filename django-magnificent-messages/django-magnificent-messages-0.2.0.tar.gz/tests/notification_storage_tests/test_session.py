from django.http import HttpRequest
from django.test import TestCase
from django.utils.safestring import SafeData, mark_safe

from django_magnificent_messages import constants
from django_magnificent_messages.storage.base import Message
from django_magnificent_messages.storage.notification_storage.session import SessionStorage
from .base import BaseTests


def set_session_data(storage, messages):
    """
    Sets the messages into the backend request's session and remove the
    backend's loaded data cache.
    """
    storage.request.session[storage.session_key] = storage.serialize_notifications(messages)
    if hasattr(storage, '_loaded_data'):
        del storage._loaded_data


def stored_session_notifications_count(storage):
    data = storage.deserialize_notifications(storage.request.session.get(storage.session_key, []))
    return len(data)


class SessionTests(BaseTests, TestCase):
    storage_class = SessionStorage

    def get_request(self):
        self.session = {}
        request = super().get_request()
        request.session = self.session
        return request

    def stored_notifications_count(self, storage, response):
        return stored_session_notifications_count(storage)

    def test_no_session(self):
        msg = (
            'The session-based temporary notification storage requires session middleware to be installed, and come '
            'before the message middleware in the MIDDLEWARE list.'
        )
        with self.assertRaisesMessage(AssertionError, msg):
            self.storage_class(HttpRequest())

    def test_get(self):
        storage = self.storage_class(self.get_request())
        example_messages = ['test', 'me']
        set_session_data(storage, example_messages)
        self.assertEqual(list(storage), example_messages)

    def test_safedata(self):
        """
        A text containing SafeData keeps its safe status when retrieved from
        the text notification_storage.
        """
        storage = self.get_storage()
        message = Message(constants.SECONDARY, mark_safe("<b>Hello Django!</b>"))
        set_session_data(storage, [message])
        self.assertIsInstance(list(storage)[0].text, SafeData)