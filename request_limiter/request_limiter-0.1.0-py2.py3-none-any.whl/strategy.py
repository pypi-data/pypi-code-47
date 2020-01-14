import abc
import time
from typing import Callable, Optional


class LimitStrategy(metaclass=abc.ABCMeta):
    """
    A request limit strategy abstract class
    """
    @abc.abstractmethod
    def request(self, key: Optional[str] = None) -> bool:
        """
        Checks if it can allocate one request
        :return: True if it can allocate else False
        """
        pass

    @abc.abstractmethod
    def get_remaining(self, key: Optional[str] = None) -> float:
        """
        Returns the remaining seconds for the next request window
        :return: time in seconds
        """
        pass

    @abc.abstractmethod
    def clean(self):
        """
        Clean expired keys from storage
        """
        pass


class LimitedIntervalStrategy(LimitStrategy):
    DEFAULT_KEY = 'default'

    def __init__(self, requests: Optional[int] = 100, interval: Optional[int] = 24 * 60 * 60,
                 now: Optional[Callable[[], float]] = time.monotonic, storage: Optional[dict] = None):
        self.requests = requests
        self.interval = interval
        self.now = now
        self.storage = storage if storage is not None else {}

    def request(self, key: Optional[str] = None) -> bool:
        """
        Allocates one request in current window for the key
        :param key: Storage key
        :return: True if allocated else False
        """
        key = key or self.DEFAULT_KEY
        remaining_time = self.get_remaining(key)
        if remaining_time <= 0:
            # new interval window, reset strategy
            self._reset(key)

        # increment request count and check if it pass the limit
        self.storage[key]['request_count'] += 1
        if self.storage[key]['request_count'] > self.requests:
            return False

        return True

    def get_remaining(self, key: Optional[str] = None) -> float:
        """
        Returns the remaining seconds for the next request window
        :param key: Storage key
        :return: Remaining seconds
        """
        key = key or self.DEFAULT_KEY
        self._init(key)
        store = self.storage[key]
        spent_time = self.now() - store['reset_time']
        return self.interval - spent_time

    def clean(self):
        """
        Remove expired keys from the storage
        """
        while True:
            expired_keys = []
            for key, store in self.storage.items():
                if self.now() - store['reset_time'] > self.interval and key != self.DEFAULT_KEY:
                    expired_keys.append(key)

            [self.storage.pop(key) for key in expired_keys]  # delete keys
            time.sleep(self.interval)  # Check every interval period

    def _init(self, key: str):
        """
        Initialize storage for a key, if it is missing
        """
        if key not in self.storage:
            self.storage[key] = {}
            self._reset(key)

    def _reset(self, key: str):
        """
        Reset the storage for a key
        """
        self.storage[key]['request_count'] = 0
        self.storage[key]['reset_time'] = self.now()
