from typing import Iterable

from django_magnificent_messages import models
from django_magnificent_messages.storage.base import StorageError, Message
from django_magnificent_messages.storage.message_storage.base import BaseMessageStorage, StoredMessage
from django_magnificent_messages.storage.message_storage.db_signals import message_sent


class DatabaseStorage(BaseMessageStorage):
    """
    Database Message Storage

    Stores messages in database in Message model. Access to user messages provided through Inbox model, which handles
    storing last check date
    """

    def _get_sent_messages(self) -> Iterable:
        pass

    def _get_sent_messages_count(self) -> int:
        pass

    def __init__(self, request, *args, **kwargs):
        super(DatabaseStorage, self).__init__(request, *args, **kwargs)
        try:
            if request.user.is_authenticated:
                self.user = request.user
                self._inbox, _ = models.Inbox.objects.get_or_create(user=request.user, main=True)
            else:
                self.user = None
                self._inbox = None
        except AttributeError:
            self.user = None
            self._inbox = None
        except models.Inbox.MultipleObjectsReturned:
            raise StorageError(self.__class__.__name__, "User `{0}` has more then one main inbox".format(request.user))

    def _get_all_messages(self) -> Iterable:
        return getattr(self._inbox, "all", [])

    def _get_read_messages(self) -> Iterable:
        return getattr(self._inbox, "read", [])

    def _get_unread_messages(self) -> Iterable:
        return getattr(self._inbox, "unread", [])

    def _get_archived_messages(self) -> Iterable:
        return getattr(self._inbox, "archived", [])

    def _get_new_messages(self) -> Iterable:
        return getattr(self._inbox, "new", [])

    def _get_all_messages_count(self) -> int:
        return getattr(self._inbox, "all_count", 0)

    def _get_read_messages_count(self) -> int:
        return getattr(self._inbox, "read_count", 0)

    def _get_unread_messages_count(self) -> int:
        return getattr(self._inbox, "unread_count", 0)

    def _get_archived_messages_count(self) -> int:
        return getattr(self._inbox, "archived_count", 0)

    def _get_new_messages_count(self) -> int:
        return getattr(self._inbox, "new_count", 0)

    def _get_new_messages_count_update_last_check(self):
        return getattr(self._inbox, "new_count_update_last_checked", 0)

    def _save_message(self, message: Message, author_pk, to_users_pk: Iterable, to_groups_pk: Iterable,
                      user_generated: bool = True, html_safe: bool = False, reply_to_pk=None) -> StoredMessage:
        try:
            reply_to = models.Message.objects.get(pk=reply_to_pk)
        except models.Message.DoesNotExist:
            reply_to = None
        new_message = models.Message(
            level=message.level,
            raw_text=message.text,
            author_id=author_pk,
            subject=message.subject,
            extra=message.extra,
            reply_to=reply_to,
            user_generated=user_generated,
            html_safe=html_safe
        )
        new_message.save()
        new_message.sent_to_users.set(to_users_pk)
        new_message.sent_to_groups.set(to_groups_pk)
        message_sent.send(sender=self.__class__, message=new_message)
        return self._stored_to_message(new_message)

    def _stored_to_message(self, stored: models.Message) -> StoredMessage:
        """
        Convert message from internal storage representation to StoredMessage instance
        """
        return StoredMessage(
            stored.level,
            stored.text,
            stored.subject,
            raw_text=stored.raw_text,
            extra=stored.extra,
            author=stored.author,
            user_generated=stored.user_generated,
            reply_to=stored.reply_to,
            pk=stored.pk,
            created=stored.created,
            modified=stored.modified
        )
