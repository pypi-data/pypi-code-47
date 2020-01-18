# -*- coding: utf-8 -*-

import time
import logging
from pprint import pformat
from os.path import basename
from utils import Config


class Logger(Config):
    _format = None
    _file = None
    _handler = None
    _bad_logger = None
    _bad_file = None
    _buffer = []

    def __init__(self):
        Config.__init__(self)
        logging.Logger(basename(self.script), logging.INFO)

        # Formato da linha de log
        if "log" in self.conf and "format" in self.conf["log"]:
            # Le do arquivo de configuracao
            self._format = self.conf["log"]["format"]
        else:
            # Formato padrao
            self._format = "%(asctime)-15s %(name) %(levelname)s %(message)s"

        # Arquivo de log no disco
        # filename = re.sub(r"py$", "log", basename(self.script), 1)
        # self._file = self.dir + "/../../LOGs/" + filename
        self._file = self.dir + "/../logs/roo-broker.log"
        self._bad_file = self.dir + "/../logs/roo-broker.err"

        # Inicializacao do manipulador do log
        logging.basicConfig(
            filename=self._file,
            format=self._format,
            level=logging.INFO
        )

        formatter = logging.Formatter(self._format)
        fileHandler = logging.FileHandler(self._bad_file)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)

        self._bad_logger = logging.getLogger(self.script + "ERROR")
        self._bad_logger.setLevel(logging.ERROR)
        self._bad_logger.addHandler(fileHandler)
        self._bad_logger.addHandler(streamHandler)

    def info(self, message, data=None):
        if data:
            message += ":\n" + str(pformat(data, depth=5))

        self._add_buffer('INFO', message)
        return logging.info(message)

    def debug(self, message, data=None):
        if data:
            message += ":\n" + str(pformat(data, depth=5))

        self._add_buffer('DEBUG', message)
        return logging.debug(message)

    def error(self, message, data=None):
        if data:
            message += ":\n" + str(pformat(data, depth=5))

        self._add_buffer('ERROR', message)
        self._bad_logger.error(message)
        return logging.error(message)

    def warning(self, message, data=None):
        if data:
            message += ":\n" + str(pformat(data, depth=5))

        self._add_buffer('WARNING', message)
        return logging.warning(message)

    def get_buffer(self):
        try:
            return self._buffer
        finally:
            self._buffer = []

    def _add_buffer(self, level, message):
        self._buffer.append({
            "log_time": time.strftime("%Y-%m-%d %X"),
            "script": self.type,
            "level": level,
            "message": message,
            "dt_foto": time.strftime("%Y-%m-%d")
        })
