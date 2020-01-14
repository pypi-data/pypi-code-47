import os
import time

from abc import ABC, abstractmethod
from mountvfs.exceptions import LocalExportError, RetryExportError, TotalExportError
from typeguard import typechecked
from typing import Callable, Iterable, Optional


class Vfs(ABC):

    _FALLBACK_DEFAULT_DIR = 'mount_vfs'

    @typechecked
    def __init__(self, target_dir: str, fallback_dir: Optional[str] = None):
        """
        :param str target_dir: A path to save to; can be local or mounted.
        :param Optional[str] fallback_dir: A path to use in case of target saving failure; is "~/mount_vfs" by default.
        """
        self._target_dir = self._parse_endpoint(target_dir)
        try:
            self._fallback_dir = self._parse_endpoint(fallback_dir)
        except AssertionError:
            self._fallback_dir = os.path.join(os.path.abspath(os.path.expanduser('~')), self._FALLBACK_DEFAULT_DIR)
        os.makedirs(self._target_dir, exist_ok=True)
        os.makedirs(self._fallback_dir, exist_ok=True)

    def __enter__(self):
        try:
            self._mount()
        except Exception:
            raise
        else:
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self._unmount()
        except ConnectionError:
            print('Connection already closed.')

    @abstractmethod
    def _mount(self):
        pass

    @abstractmethod
    def _unmount(self):
        pass

    @staticmethod
    def _parse_endpoint(path: str):
        assert path, f'Endpoint {path} is empty'
        endpoint = os.path.abspath(os.path.expanduser(path))
        assert os.path.isdir(endpoint), f'"{endpoint}" is not a directory'
        assert not os.listdir(endpoint), f'"{endpoint}" is not empty'
        return endpoint

    @staticmethod
    def _sleep(ms: int):
        time.sleep(ms / 1000)

    @typechecked
    def save(self, save_func: Callable, args: Iterable = (), max_retry: int = 3, delay: int = 5000):
        """
        :param Callable save_func: a function that is called for saving.
        :param Optional[Iterable] args: save_func arguments.
        :param int max_retry: Maximum times saving is retried; must be >= 0.
        :param int delay: Milliseconds to wait until another retry; must be >= 0.
        """
        assert max_retry >= 0 and delay >= 0, 'max_retry and delay must be non-negative.'
        save_result = None

        def retry(fail_exc: Optional[type] = None, success_exc: Optional[type] = None,
                  exc_val: Optional[Exception] = None):
            for i in range(max_retry):
                try:
                    retry_result = save_func(self._target_dir, *args)
                except ConnectionError as retryExc:
                    if i >= max_retry - 1:
                        if fail_exc is not None:
                            raise fail_exc(retryExc)
                    else:
                        self._sleep(delay)
                        self._mount()
                        continue
                except Exception as retryExc:
                    if i >= max_retry - 1:
                        if fail_exc is not None:
                            raise fail_exc(retryExc)
                    else:
                        self._sleep(delay)
                        continue
                else:
                    if success_exc is not None:
                        raise success_exc if exc_val is None else success_exc(exc_val)
                    else:
                        return retry_result

        try:
            save_result = save_func(self._target_dir, *args)
        except Exception as e:
            if isinstance(e, ConnectionError):
                self._mount()
            try:
                save_func(self._fallback_dir, *args)
            except Exception as localExc:
                retry(fail_exc=TotalExportError, success_exc=LocalExportError, exc_val=localExc)
            else:
                save_result = retry(fail_exc=RetryExportError)

        return save_result
