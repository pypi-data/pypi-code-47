from django_magnificent_messages.conf import settings


class Message:
    """
    Represent an actual message that can be stored in any of the supported
    storage classes and rendered in a view or template.
    """

    def __init__(self,
                 level,
                 text,
                 subject=None,
                 extra=None,
                 **_):
        self.level = level
        self.subject = subject
        self.text = text
        self.extra = extra

    def prepare(self):
        """
        Prepare the message for serialization by forcing the ``subject`` and ``raw_text``
        to str in case they are lazy translations.
        """
        if self.subject is not None:
            self.subject = str(self.subject)
        self.text = str(self.text)

    def __eq__(self, other):
        return isinstance(other, Message) and self.level == other.level and \
            self.text == other.text and self.subject == other.subject and self.extra == other.extra

    def __str__(self):
        return str("[{0.subject}] {0.text}".format(self))

    @property
    def level_tag(self):
        return settings.DMM_LEVEL_TAGS.get(self.level, '')

    def to_dict(self):
        self.prepare()
        return {
            'level': self.level,
            'subject': self.subject,
            'text': self.text,
            'extra': self.extra
        }


class StorageError(Exception):
    def __init__(self, backend, message):
        super(StorageError, self).__init__()
        self.backend = backend
        self.message = message

    def __str__(self):
        return "[{0.backend}]: {0.message}".format(self)


class BaseStorage:
    """
    This is the base message/notification storage.

    Class contains methods used by both notification and message storages. You should use this class directly only
    if you creating another type of messages in your system. Otherwise you should subclass ``BaseNotificationStorage``
    or ``BaseMessageStorage``
    """

    def __init__(self, request, *args, **kwargs):
        self.request = request

    @staticmethod
    def _prepare_all(messages):
        """
        Prepare a list of messages/notifications for storage.
        """
        for message in messages:
            message.prepare()

    def _construct(self, level, text, subject, extra=None):
        """
        Construct message/notification.

        If message/notification body (``text`` arg) is empty or message/notification level lesser then storage
        minimal level, ``None`` will be returned. Use this method in subclasses to check and construct Message object
        before processing new message/notification.
        """
        if not text:
            return None
        # Check that the message/notification level is not less than the recording level.
        level = int(level)
        if level < self.level:
            return None
        return Message(level, text, subject=subject, extra=extra)

    def _get_level(self):
        """
        Return the minimum recorded level.

        The default level is the ``DMM_MINIMAL_LEVEL`` setting. If this is
        not found, the ``INFO`` level is used.
        """
        if not hasattr(self, '_level'):
            self._level = settings.DMM_MINIMAL_LEVEL
        return self._level

    def _set_level(self, value=None):
        """
        Set a custom minimum recorded level.

        If set to ``None``, the default level will be used (see the
        ``_get_level`` method).
        """
        if value is None and hasattr(self, '_level'):
            del self._level
        else:
            self._level = int(value)

    level = property(_get_level, _set_level, _set_level)
