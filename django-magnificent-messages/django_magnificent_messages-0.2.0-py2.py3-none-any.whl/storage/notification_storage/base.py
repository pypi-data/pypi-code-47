from django_magnificent_messages.storage.base import BaseStorage


class BaseNotificationStorage(BaseStorage):
    """
    This is the base notification storage.

    This is not a complete class; to be a usable storage, it must be
    subclassed and the two methods ``_get`` and ``_store`` overridden.
    """

    def __init__(self, request, *args, **kwargs):
        super(BaseNotificationStorage, self).__init__(request, *args, **kwargs)
        self.used = False
        self._queued = []
        self.added_new = False

    def __len__(self):
        return len(self._loaded) + len(self._queued)

    def _get_iterator(self):
        if self._queued:
            self._loaded.extend(self._queued)
            self._queued = []
        return iter(self._loaded)

    def __iter__(self):
        self.used = True
        return self._get_iterator()

    @property
    def _loaded(self):
        """
        Return a list of loaded notifications, retrieving them first if they have
        not been loaded yet.
        """
        if not hasattr(self, '_loaded_data'):
            messages, all_retrieved = self._get()
            self._loaded_data = messages or []
        return self._loaded_data

    def _get(self, *args, **kwargs):
        """
        Retrieve a list of stored notifications. Return a tuple of the notifications
        and a flag indicating whether or not all the notifications originally
        intended to be stored in this storage were, in fact, stored and
        retrieved; e.g., ``(notifications, all_retrieved)``.

        **This method must be implemented by a subclass.**

        If it is possible to tell if the backend was not used (as opposed to
        just containing no notifications) then ``None`` should be returned in
        place of ``notifications``.
        """
        raise NotImplementedError('subclasses of BaseNotificationStorage must provide a _get() method')

    def _store(self, notifications, response, *args, **kwargs):
        """
        Store a list of notifications and return a list of any notifications which could
        not be stored.

        One type of object must be able to be stored, ``Message``.

        **This method must be implemented by a subclass.**
        """
        raise NotImplementedError('subclasses of BaseNotificationStorage must provide a _store() method')

    def update(self, response):
        """
        Store all unread notifications.

        If the backend has yet to be iterated, store previously stored notifications
        again. Otherwise, only store notifications added after the last iteration.
        """
        self._prepare_all(self._queued)
        if self.used:
            return self._store(self._queued, response)
        elif self.added_new:
            messages = self._loaded + self._queued
            return self._store(messages, response)

    def add(self, level: int, text: str, subject: str = None, extra=None) -> None:
        """
        Queue a notification to be stored.

        The notification is only queued if it contained something and its level is
        not less than the recording level (``self.level``).
        """
        notification = self._construct(level, text, subject, extra)
        if notification:
            self.added_new = True
            self._queued.append(notification)
