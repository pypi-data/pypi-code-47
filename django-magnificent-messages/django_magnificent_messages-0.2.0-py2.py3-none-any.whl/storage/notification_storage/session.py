import json

from django.conf import settings
from .cookie import (
    NotificationDecoder, NotificationsEncoder,
)

from django_magnificent_messages.storage.notification_storage.base import BaseNotificationStorage


class SessionStorage(BaseNotificationStorage):
    """
    Store notifications in the session (that is, django.contrib.sessions).
    """
    session_key = '_notifications'

    def __init__(self, request, *args, **kwargs):
        if not hasattr(request, 'session'):
            raise AssertionError("The session-based temporary "
                                 "notification storage requires session middleware to be installed, "
                                 "and come before the message middleware in the "
                                 "MIDDLEWARE%s list." % ("_CLASSES" if settings.MIDDLEWARE is None else ""))
        super().__init__(request, *args, **kwargs)

    def _get(self, *args, **kwargs):
        """
        Retrieve a list of notifications from the request's session. This notification storage
        always stores everything it is given, so return True for the
        all_retrieved flag.
        """
        return self.deserialize_notifications(self.request.session.get(self.session_key)), True

    def _store(self, notifications, response, *args, **kwargs):
        """
        Store a list of notifications to the request's session.
        """
        if notifications:
            self.request.session[self.session_key] = self.serialize_notifications(notifications)
        else:
            self.request.session.pop(self.session_key, None)
        return []

    @staticmethod
    def serialize_notifications(notifications):
        encoder = NotificationsEncoder(separators=(',', ':'))
        return encoder.encode(notifications)

    @staticmethod
    def deserialize_notifications(data):
        if data and isinstance(data, str):
            return json.loads(data, cls=NotificationDecoder)
        return data
