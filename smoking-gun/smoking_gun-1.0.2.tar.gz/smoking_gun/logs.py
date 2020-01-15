import logging
from collections import deque


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


MAX_LOG_LINES = 1000000
DEFAULT_LOG_LINES = 1000


class CapturedLogging(object):
    def __init__(self, max_len=DEFAULT_LOG_LINES):
        self.__handlers = deque([])
        self.__log_kwargs = {}
        max_len = max_len if max_len is not None else DEFAULT_LOG_LINES
        max_len = max_len if max_len >= 0 else DEFAULT_LOG_LINES
        max_len = min([abs(max_len), MAX_LOG_LINES])
        self._logs = deque(maxlen=max_len)

    def __enter__(self):
        self.__log_kwargs["stream"] = StringIO()
        if logging.root and logging.root.handlers:
            for handler in logging.root.handlers:
                self._copy_handler(handler)
                logging.root.removeHandler(handler)
        logging.basicConfig(**self.__log_kwargs)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._read_logs()
        del self.__log_kwargs["stream"]
        if self.__handlers:
            for handler in logging.root.handlers:
                logging.root.removeHandler(handler)
            for handler in self.__handlers:
                logging.root.addHandler(handler)

    def _read_logs(self):
        try:
            stream = self.__log_kwargs["stream"]
            stream.seek(0)
            self._logs.extend(stream.readlines())
        except KeyError:
            self._logs.clear()

    def _copy_handler(self, handler):
        if self.__log_kwargs.get("format") is None:
            self.__log_kwargs["format"] = handler.formatter._fmt
        if self.__log_kwargs.get("datefmt") is None:
            self.__log_kwargs["datefmt"] = handler.formatter.datefmt
        if self.__log_kwargs.get("level") is None:
            self.__log_kwargs["level"] = (
                handler.level if handler.level < logging.DEBUG else logging.DEBUG
            )
        self.__handlers.append(handler)

    @property
    def logs(self):
        return "".join(self._logs)
