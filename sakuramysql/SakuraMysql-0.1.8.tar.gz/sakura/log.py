import logging
import sys


class LoggingFactory:
    def __init__(self, name, loglevel=logging.DEBUG, logfile=None, stdout=False):
        self.name = name
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        _logger = logging.getLogger(self.name)
        _logger.setLevel(level=loglevel)

        file_logger = logfile and logging.FileHandler(logfile)
        stdout_logger = stdout and logging.StreamHandler(sys.stdout)

        stdout_logger and stdout_logger.setLevel(loglevel)
        stdout_logger and stdout_logger.setFormatter(formatter)
        stdout_logger and _logger.addHandler(stdout_logger)

        file_logger and file_logger.setLevel(loglevel)
        file_logger and file_logger.setFormatter(formatter)
        file_logger and _logger.addHandler(file_logger)

    @property
    def logger(self):
        return logging.getLogger(self.name)


logger = LoggingFactory('sakura', stdout=True).logger
