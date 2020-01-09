import logging


class LoggingFormatter(logging.Formatter):

    debug_format = '[%(asctime)s]::%(levelname)s::%(filename)s::%(funcName)s::%(lineno)d    %(message)s'
    info_format = '[%(asctime)s]::%(levelname)s    %(message)s'
    warning_format = '[%(asctime)s]::%(levelname)s::%(filename)s::%(funcName)s::%(lineno)d    %(message)s'
    error_format = '[%(asctime)s]::%(levelname)s::%(filename)s::%(funcName)s::%(lineno)d    %(message)s'

    def __init__(self):
        super().__init__(fmt="%(levelno)s: %(msg)s", datefmt='%Y.%m.%d-%H:%M:%S')

    def format(self, record):
        format_orig = self._style._fmt
        if record.levelno == logging.DEBUG:
            self._style._fmt = LoggingFormatter.debug_format
        elif record.levelno == logging.INFO:
            self._style._fmt = LoggingFormatter.info_format
        elif record.levelno == logging.WARNING:
            self._style._fmt = LoggingFormatter.warning_format
        elif record.levelno == logging.ERROR:
            self._style._fmt = LoggingFormatter.error_format
        result = logging.Formatter.format(self, record)
        self._style._fmt = format_orig
        return result


class Logger():

    def __init__(self, log_level=logging.INFO):
        logger = logging.StreamHandler()
        logger.setFormatter(LoggingFormatter())
        logging.root.addHandler(logger)
        logging.root.setLevel(log_level)
