from typing import Iterable

from django.utils.module_loading import import_string

from django_magnificent_messages.storage.message_storage.base import BaseMessageStorage
from django_magnificent_messages.storage.notification_storage.base import BaseNotificationStorage
from .conf import settings as config


class MessageBackend:
    def __init__(self, request):
        self._notification_storage = \
            import_string(config.DMM_NOTIFICATION_STORAGE)(request)  # type: BaseNotificationStorage
        self._message_storage = import_string(config.DMM_MESSAGE_STORAGE)(request)  # type: BaseMessageStorage

    @property
    def notifications(self) -> Iterable:
        """Get notifications iterable"""
        return self._notification_storage

    @property
    def notifications_count(self) -> int:
        """Get notifications count"""
        return len(self._notification_storage)

    @property
    def all_messages(self) -> Iterable:
        """Get all messages"""
        return self._message_storage.all

    @property
    def read_messages(self) -> Iterable:
        """Get read messages"""
        return self._message_storage.read

    @property
    def unread_messages(self) -> Iterable:
        """Get unread messages"""
        return self._message_storage.unread

    @property
    def archived_messages(self) -> Iterable:
        """Get archived messages"""
        return self._message_storage.archived

    @property
    def new_messages(self) -> Iterable:
        """Get new messages"""
        return self._message_storage.new

    @property
    def all_messages_count(self) -> int:
        """Get all messages count"""
        return self._message_storage.all_count

    @property
    def read_messages_count(self) -> int:
        """Get read messages count"""
        return self._message_storage.read_count

    @property
    def unread_messages_count(self) -> int:
        """Get unread messages count"""
        return self._message_storage.unread_count

    @property
    def archived_messages_count(self) -> int:
        """Get archived messages count"""
        return self._message_storage.archived_count

    @property
    def new_messages_count(self) -> int:
        """Get new messages count"""
        return self._message_storage.new_count

    @property
    def new_messages_count_update_last_checked(self) -> int:
        """Get new messages count"""
        return self._message_storage.new_count_update_last_checked

    def get_level(self) -> int:
        """Get minimal stored message/notification level"""
        return min(self._notification_storage.level, self._message_storage.level)

    def set_level(self, level: int) -> None:
        """Set minimal stored message/notification level"""
        self._notification_storage.level = level
        self._message_storage.level = level

    def add_notification(self, level: int, text: str, subject: str = None, extra=None) -> None:
        """Add new notification with specified level"""
        self._notification_storage.add(level, text, subject, extra)

    def send_message(self,
                     level: int,
                     text: str,
                     subject: str = None,
                     extra: object = None,
                     to_users_pk: Iterable = tuple(),
                     to_groups_pk: Iterable = tuple(),
                     user_generated: bool = True,
                     html_safe: bool = False,
                     reply_to_pk=None) -> None:
        """Add new message with specified level"""
        self._message_storage.send_message(level, text, subject, extra, to_users_pk, to_groups_pk, user_generated,
                                           html_safe, reply_to_pk)

    def update(self, response):
        return self._notification_storage.update(response)
