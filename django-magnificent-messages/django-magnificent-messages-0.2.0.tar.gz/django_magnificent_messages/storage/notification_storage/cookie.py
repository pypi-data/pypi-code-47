import json

from django import VERSION
from django.conf import settings

from .base import BaseNotificationStorage
from ..base import Message
from django.http import SimpleCookie
from django.utils.crypto import constant_time_compare, salted_hmac
from django.utils.safestring import SafeData, mark_safe


class NotificationsEncoder(json.JSONEncoder):
    """
    Compactly serialize instances of the ``Message`` class as JSON.
    """
    message_key = '__json_notification'

    def default(self, obj):
        if isinstance(obj, Message):
            # Using 0/1 here instead of False/True to produce more compact json
            is_safe_data = 1 if isinstance(obj.text, SafeData) else 0
            message = [self.message_key, is_safe_data, obj.level, obj.text, obj.subject, obj.extra]
            return message
        return super().default(obj)


class NotificationDecoder(json.JSONDecoder):
    """
    Decode JSON that includes serialized ``Message`` instances.
    """

    def process_notifications(self, obj):
        if isinstance(obj, list) and obj:
            if obj[0] == NotificationsEncoder.message_key:
                if obj[1]:
                    obj[3] = mark_safe(obj[3])
                return Message(*obj[2:])
            return [self.process_notifications(item) for item in obj]
        if isinstance(obj, dict):
            return {key: self.process_notifications(value)
                    for key, value in obj.items()}
        return obj

    def decode(self, s, **kwargs):
        decoded = super().decode(s, **kwargs)
        return self.process_notifications(decoded)


class CookieStorage(BaseNotificationStorage):
    """
    Store messages in a cookie.
    """
    cookie_name = 'notifications'
    # uwsgi's default configuration enforces a maximum size of 4kb for all the
    # HTTP headers. In order to leave some room for other cookies and headers,
    # restrict the session cookie to 1/2 of 4kb. See #18781.
    max_cookie_size = 2048
    not_finished = '__notificationsnotfinished__'

    def _get(self, *args, **kwargs):
        """
        Retrieve a list of notifications from the notifications cookie. If the
        not_finished sentinel value is found at the end of the notification list,
        remove it and return a result indicating that not all notifications were
        retrieved by this notification storage.
        """
        data = self.request.COOKIES.get(self.cookie_name)
        notifications = self._decode(data)
        all_retrieved = not (notifications and notifications[-1] == self.not_finished)
        if notifications and not all_retrieved:
            # remove the sentinel value
            notifications.pop()
        return notifications, all_retrieved

    def _update_cookie(self, encoded_data, response):
        """
        Either set the cookie with the encoded data if there is any data to
        store, or delete the cookie.
        """
        if encoded_data:
            if VERSION[:2] == (2, 0):
                response.set_cookie(
                    self.cookie_name, encoded_data,
                    domain=settings.SESSION_COOKIE_DOMAIN,
                    secure=settings.SESSION_COOKIE_SECURE or None,
                    httponly=settings.SESSION_COOKIE_HTTPONLY or None,
                )
            else:
                response.set_cookie(
                    self.cookie_name, encoded_data,
                    domain=settings.SESSION_COOKIE_DOMAIN,
                    secure=settings.SESSION_COOKIE_SECURE or None,
                    httponly=settings.SESSION_COOKIE_HTTPONLY or None,
                    samesite=settings.SESSION_COOKIE_SAMESITE,
                )
        else:
            response.delete_cookie(self.cookie_name, domain=settings.SESSION_COOKIE_DOMAIN)

    def _store(self, notifications, response, remove_oldest=True, *args, **kwargs):
        """
        Store the notifications to a cookie and return a list of any notifications which
        could not be stored.

        If the encoded data is larger than ``max_cookie_size``, remove
        notifications until the data fits (these are the notifications which are
        returned), and notifications_add the not_finished sentinel value to indicate as much.
        """
        unstored_notifications = []
        encoded_data = self._encode(notifications)
        if self.max_cookie_size:
            # data is going to be stored eventually by SimpleCookie, which
            # adds its own overhead, which we must account for.
            cookie = SimpleCookie()  # create outside the loop

            def stored_length(val):
                return len(cookie.value_encode(val)[1])

            while encoded_data and stored_length(encoded_data) > self.max_cookie_size:
                if remove_oldest:
                    unstored_notifications.append(notifications.pop(0))
                else:
                    unstored_notifications.insert(0, notifications.pop())
                encoded_data = self._encode(notifications + [self.not_finished],
                                            encode_empty=bool(unstored_notifications))
        self._update_cookie(encoded_data, response)
        return unstored_notifications

    @staticmethod
    def _hash(value):
        """
        Create an HMAC/SHA1 hash based on the value and the project setting's
        SECRET_KEY, modified to make it unique for the present purpose.
        """
        key_salt = 'django_magnificent_messages'
        return salted_hmac(key_salt, value).hexdigest()

    def _encode(self, notifications, encode_empty=False):
        """
        Return an encoded version of the notifications list which can be stored as
        plain text.

        Since the data will be retrieved from the client-side, the encoded data
        also contains a hash to ensure that the data was not tampered with.
        """
        if notifications or encode_empty:
            encoder = NotificationsEncoder(separators=(',', ':'))
            value = encoder.encode(notifications)
            return '%s$%s' % (self._hash(value), value)

    def _decode(self, data):
        """
        Safely decode an encoded text stream back into a list of notifications.

        If the encoded text stream contained an invalid hash or was in an
        invalid format, return None.
        """
        if not data:
            return None
        bits = data.split('$', 1)
        if len(bits) == 2:
            _hash, value = bits
            if constant_time_compare(_hash, self._hash(value)):
                try:
                    # If we get here (and the JSON decode works), everything is
                    # good. In any other case, drop back and return None.
                    return json.loads(value, cls=NotificationDecoder)
                except json.JSONDecodeError:
                    pass
        # Mark the data as used (so it gets removed) since something was wrong
        # with the data.
        self.used = True
        return None
