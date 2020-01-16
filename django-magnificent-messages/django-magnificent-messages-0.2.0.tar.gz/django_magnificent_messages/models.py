"""
Models for django_magnificent_messages
"""
from functools import wraps

from django.db import models
from django.db.models import Q, QuerySet
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.functional import SimpleLazyObject
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from model_utils.models import TimeStampedModel

from django_magnificent_messages import constants
from django_magnificent_messages.fields import JSONField
from .conf import settings
from .storage.message_storage.db_signals import message_archived, message_read, message_unarchived, message_unread


class MessageNotSentToUserError(Exception):
    pass


class Message(TimeStampedModel):
    """
    Main model for app.

    Stores one record for every message in system
    """
    level = models.IntegerField()

    subject = models.TextField(blank=True, null=True)
    raw_text = models.TextField()
    extra = JSONField(blank=True, null=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="outbox")
    user_generated = models.BooleanField()

    reply_to = models.ForeignKey('django_magnificent_messages.Message', on_delete=models.PROTECT,
                                 related_name="replies", null=True)
    sent_to_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="messages",
                                           db_table="mm_message_sent_to_user")
    sent_to_groups = models.ManyToManyField('auth.Group', related_name="messages", db_table="mm_message_sent_to_group")
    read_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="read_messages",
                                     db_table="mm_message_read_by_user")
    archived_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="archived_messages",
                                         db_table="mm_message_archived_by_user")
    html_safe = models.BooleanField(default=False)

    @property
    def text(self):
        if self.html_safe:
            return mark_safe(self.raw_text)
        return self.raw_text

    class Meta:
        db_table = "mm_message"
        default_permissions = ()
        permissions = (
            ("send_message", "Send message"),
            ("view_all_message", "View all messages"),
            ("delete_any_message", "Delete any messages"),
        )
        ordering = ("-created",)

    def _is_user_in_recipients(self, user):
        if user in self.sent_to_users.all():
            return True
        if hasattr(user, "groups"):
            for group in user.groups.all():
                if group in self.sent_to_groups.all():
                    return True
        return False

    def archive(self, user):

        if self._is_user_in_recipients(user):
            self.archived_by.add(user)
            message_archived.send(sender=self.__class__, message=self, user=user)
        else:
            raise MessageNotSentToUserError(
                "{0} was not sent to user, who tried to archive it".format(self)
            )

    def unarchive(self, user):

        if self._is_user_in_recipients(user):
            self.archived_by.remove(user)
            message_unarchived.send(sender=self.__class__, message=self, user=user)
        else:
            raise MessageNotSentToUserError(
                "{0} was not sent to user, who tried to unarchive ir".format(self)
            )

    def mark_read(self, user):
        if self._is_user_in_recipients(user):
            self.read_by.add(user)
            message_read.send(sender=self.__class__, message=self, user=user)
        else:
            raise MessageNotSentToUserError(
                "{0} was not sent to user, who tried to mark it as read".format(self)
            )

    def mark_unread(self, user):
        if self._is_user_in_recipients(user):
            self.read_by.remove(user)
            message_unread.send(sender=self.__class__, message=self, user=user)
        else:
            raise MessageNotSentToUserError(
                "{0} was not sent to user, who tried to mark it as unread".format(self)
            )

    def __str__(self):
        return "<Message: {0}>".format(self.pk)


class Inbox(models.Model):
    """
    Inbox model.

    Represents user inbox. Stores time, when inbox was checked last and provides methods for getting messages in inbox.

    It's possible that in future django-magnificent-messages will support multiple inboxes, so we use ForeignKey
    instead of OneToOneField and Inbox has field ``name`` with default="Inbox"
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="inboxes")
    name = models.CharField(max_length=200, default="Inbox")
    main = models.BooleanField(default=False)
    desc = models.TextField(blank=True)
    last_checked = models.DateTimeField(default=constants.MIN_DATETIME)

    @property
    def all(self) -> SimpleLazyObject:
        return self._all()

    @property
    def all_count(self) -> int:
        return self._all(set_last_checked=False).count()

    @property
    def read(self) -> SimpleLazyObject:
        return self._read(set_last_checked=False)

    @property
    def read_count(self) -> int:
        return self._read(set_last_checked=False).count()

    @property
    def unread(self) -> SimpleLazyObject:
        return self._unread()

    @property
    def unread_count(self) -> int:
        return self._unread(set_last_checked=False).count()

    @property
    def archived(self) -> SimpleLazyObject:
        return self._get_messages_lazy(set_last_checked=False, archived=True)

    @property
    def archived_count(self) -> int:
        return self.archived.count()

    @property
    def new(self):
        return self._new()

    @property
    def new_count(self):
        return self._new(set_last_checked=False).count()

    @property
    def new_count_update_last_checked(self):
        return self._new().count()

    class Meta:
        db_table = "mm_inbox"
        unique_together = (
            ("user", "name")
        )

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """
        Preventing more than one main inbox
        """
        if self.main and Inbox.objects.filter(user=self.user, main=True).exclude(pk=self.pk).exists():
            raise ValidationError(
                _("User %(user)s already has main inbox"),
                code="invalid",
                params={
                    "user": str(self.user)
                }
            )
        super(Inbox, self).save(force_insert, force_update, using, update_fields)

    def _get_messages(self, set_last_checked: bool = True, archived: bool = False, q: Q = Q()) -> QuerySet:
        """
        Get messages in this inbox and filter them with q.

        Get messages sent to user directly or through some of user groups. Excepts archived messages

        Uses two queries to avoid duplication of messages sent to user directly and through the groups, or through
        two and more groups. Can't use distinct() because Oracle does not support distinct on NCLOB fields and
        Message model has such fields (subject, raw_text and extra)

        **You should not use this method directly. Use properties instead**

        :param set_last_checked: should method update last_checked?
        :param archived: If False (default) - exclude archived. If true - notifications_show only archived
        :param q: Q object to filter messages
        :return:
        """
        # Update last checked
        if set_last_checked:
            self.last_checked = timezone.now()
            self.save()

        # Get distinct messages pks
        to_user_q = Q(sent_to_users=self.user)
        if hasattr(self.user, "groups") and hasattr(self.user.groups, "all") and callable(self.user.groups.all):
            to_user_q = to_user_q | Q(sent_to_groups__pk__in=list(self.user.groups.values_list("pk", flat=True)))
        message_pks = Message.objects.filter(to_user_q).values("id").distinct()

        # Get messages with pk in message_pks
        messages = Message.objects.filter(pk__in=message_pks)

        if archived:
            messages = messages.filter(archived_by=self.user)
        else:
            messages = messages.exclude(archived_by=self.user)

        messages = messages.filter(q)

        return messages

    def _get_messages_lazy(self, set_last_checked: bool = True, archived: bool = False,
                           q: Q = Q()) -> SimpleLazyObject:
        """
        Lazy version of _get_messages
        """

        @wraps(self._get_messages)
        def f():
            return self._get_messages(set_last_checked, archived, q)

        return SimpleLazyObject(f)

    def _all(self, set_last_checked: bool = True) -> SimpleLazyObject:
        """
        Returns all messages in inbox except archived
        """
        return self._get_messages_lazy(set_last_checked)

    def _read(self, set_last_checked: bool = True) -> SimpleLazyObject:
        return self._get_messages_lazy(set_last_checked,
                                       q=Q(pk__in=self.user.read_messages.values("pk")))

    def _unread(self, set_last_checked: bool = True) -> SimpleLazyObject:
        return self._get_messages_lazy(set_last_checked,
                                       q=~Q(pk__in=self.user.read_messages.values("pk")))

    def _new(self, set_last_checked: bool = True) -> SimpleLazyObject:
        """
        Returns all messages in inbox except archived
        """
        return self._get_messages_lazy(set_last_checked, q=Q(created__gt=self.last_checked))
