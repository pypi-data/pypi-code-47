import logging
from collections import deque


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class CapturedLogging(object):
    def __init__(self):
        self.__handlers = deque([])
        self.__log_kwargs = {}
        self.logs = None

    def __enter__(self):
        self.__log_kwargs["stream"] = StringIO()
        if logging.root and logging.root.handlers:
            for handler in logging.root.handlers:
                self._copy_handler(handler)
                logging.root.removeHandler(handler)
        logging.basicConfig(**self.__log_kwargs)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logs = self._read_logs()
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
            return stream.read()
        except KeyError:
            return ""

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
