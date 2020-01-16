from .base import BaseNotificationStorage
from .cookie import CookieStorage
from .session import SessionStorage


class FallbackStorage(BaseNotificationStorage):
    """
    Try to store all notifications in the first storage. Store any unstored
    messages in each subsequent storages.
    """
    storage_classes = (CookieStorage, SessionStorage)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.storages = [storage_class(*args, **kwargs)
                         for storage_class in self.storage_classes]
        self._used_storages = set()

    def _get(self, *args, **kwargs):
        """
        Get a single list of notifications from all notification storages.
        """
        all_notifications = []
        all_retrieved = False
        for storage in self.storages:
            notifications, all_retrieved = storage._get()
            # If the backend hasn't been used, no more retrieval is necessary.
            if notifications is None:
                break
            if notifications:
                self._used_storages.add(storage)
            all_notifications.extend(notifications)
            # If this notification_storage class contained all the messages, no further
            # retrieval is necessary
            if all_retrieved:
                break
        return all_notifications, all_retrieved

    def _store(self, notifications, response, *args, **kwargs):
        """
        Store the notifications and return any unstored notifications after trying all
        backends.

        For each notification storage, any notifications not stored are passed on to the
        next backend.
        """
        for storage in self.storages:
            if notifications:
                notifications = storage._store(notifications, response, remove_oldest=False)
            # Even if there are no more messages, continue iterating to ensure
            # storages which contained messages are flushed.
            elif storage in self._used_storages:
                storage._store([], response)
                self._used_storages.remove(storage)
        return notifications
