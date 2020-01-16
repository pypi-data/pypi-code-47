import json

import django

from django_magnificent_messages import constants
from django_magnificent_messages.storage.base import Message
from django_magnificent_messages.storage.notification_storage.cookie import (
    CookieStorage, NotificationDecoder, NotificationsEncoder,
)
from django.test import SimpleTestCase, override_settings
from django.utils.safestring import SafeData, mark_safe

from .base import BaseTests


def set_cookie_data(storage, messages, invalid=False, encode_empty=False):
    """
    Set ``request.COOKIES`` with the encoded data and remove the notification_storage
    backend's loaded data cache.
    """
    encoded_data = storage._encode(messages, encode_empty=encode_empty)
    if invalid:
        # Truncate the first character so that the hash is invalid.
        encoded_data = encoded_data[1:]
    storage.request.COOKIES = {CookieStorage.cookie_name: encoded_data}
    if hasattr(storage, '_loaded_data'):
        del storage._loaded_data


def stored_cookie_notifications_count(storage, response):
    """
    Return an integer containing the number of messages stored.
    """
    # Get a list of cookies, excluding ones with a max-age of 0 (because
    # they have been marked for deletion).
    cookie = response.cookies.get(storage.cookie_name)
    if not cookie or cookie['max-age'] == 0:
        return 0
    data = storage._decode(cookie.value)
    if not data:
        return 0
    if data[-1] == CookieStorage.not_finished:
        data.pop()
    return len(data)


@override_settings(SESSION_COOKIE_DOMAIN='.example.com', SESSION_COOKIE_SECURE=True, SESSION_COOKIE_HTTPONLY=True)
class CookieTests(BaseTests, SimpleTestCase):
    storage_class = CookieStorage

    def stored_notifications_count(self, storage, response):
        return stored_cookie_notifications_count(storage, response)

    def test_get(self):
        storage = self.storage_class(self.get_request())
        # Set initial data.
        example_messages = ['test', 'me']
        set_cookie_data(storage, example_messages)
        self.assertEqual(list(storage), example_messages)

    @override_settings(SESSION_COOKIE_SAMESITE='Strict')
    def test_cookie_setings(self):
        """
        CookieStorage honors SESSION_COOKIE_DOMAIN, SESSION_COOKIE_SECURE, and
        SESSION_COOKIE_HTTPONLY (#15618, #20972).
        """
        # Test before the messages have been consumed
        storage = self.get_storage()
        response = self.get_response()
        storage.add(constants.INFO, 'test')
        storage.update(response)
        self.assertIn('test', response.cookies['notifications'].value)
        self.assertEqual(response.cookies['notifications']['domain'], '.example.com')
        self.assertEqual(response.cookies['notifications']['expires'], '')
        self.assertIs(response.cookies['notifications']['secure'], True)
        self.assertIs(response.cookies['notifications']['httponly'], True)
        if django.VERSION[:2] != (2, 0):
            self.assertEqual(response.cookies['notifications']['samesite'], 'Strict')

        # Test deletion of the cookie (storing with an empty value) after the messages have been consumed
        storage = self.get_storage()
        response = self.get_response()
        storage.add(constants.INFO, 'test')
        for m in storage:
            pass  # Iterate through the notification_storage to simulate consumption of messages.
        storage.update(response)
        self.assertEqual(response.cookies['notifications'].value, '')
        self.assertEqual(response.cookies['notifications']['domain'], '.example.com')
        if django.VERSION[:2] == (2, 0):
            self.assertEqual(response.cookies['notifications']['expires'], 'Thu, 01-Jan-1970 00:00:00 GMT')
        else:
            self.assertEqual(response.cookies['notifications']['expires'], 'Thu, 01 Jan 1970 00:00:00 GMT')

    def test_get_bad_cookie(self):
        request = self.get_request()
        storage = self.storage_class(request)
        # Set initial (invalid) data.
        example_messages = ['test', 'me']
        set_cookie_data(storage, example_messages, invalid=True)
        self.assertEqual(list(storage), [])

    def test_max_cookie_length(self):
        """
        If the data exceeds what is allowed in a cookie, older messages are
        removed before saving (and returned by the ``update`` method).
        """
        storage = self.get_storage()
        response = self.get_response()

        # When storing as a cookie, the cookie has constant overhead of approx
        # 54 chars, and each text has a constant overhead of about 37 chars
        # and a variable overhead of zero in the best case. We aim for a text
        # size which will fit 4 messages into the cookie, but not 5.
        # See also FallbackTest.test_session_fallback
        msg_size = int((CookieStorage.max_cookie_size - 54) / 4.5 - 37)
        for i in range(5):
            storage.add(constants.INFO, str(i) * msg_size)
        unstored_messages = storage.update(response)

        cookie_storing = self.stored_notifications_count(storage, response)
        self.assertEqual(cookie_storing, 4)

        self.assertEqual(len(unstored_messages), 1)
        self.assertEqual(unstored_messages[0].text, '0' * msg_size)

    def test_json_encoder_decoder(self):
        """
        A complex nested data structure containing Message
        instances is properly encoded/decoded by the custom JSON
        encoder/decoder classes.
        """
        messages = [
            {
                'text': Message(constants.INFO, 'Test text'),
                'message_list': [
                    Message(constants.INFO, 'text %s') for x in range(5)
                ] + [{'another-text': Message(constants.ERROR, 'error')}],
            },
            Message(constants.INFO, 'text %s'),
        ]
        encoder = NotificationsEncoder(separators=(',', ':'))
        value = encoder.encode(messages)
        decoded_messages = json.loads(value, cls=NotificationDecoder)
        self.assertEqual(messages, decoded_messages)

    def test_safedata(self):
        """
        A text containing SafeData is keeping its safe status when
        retrieved from the text notification_storage.
        """
        def encode_decode(data):
            text = Message(constants.INFO, data)
            encoded = storage._encode(text)
            decoded = storage._decode(encoded)
            return decoded.text

        storage = self.get_storage()
        self.assertIsInstance(encode_decode(mark_safe("<b>Hello Django!</b>")), SafeData)
        self.assertNotIsInstance(encode_decode("<b>Hello Django!</b>"), SafeData)

