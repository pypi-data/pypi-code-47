import logging


class Logger:
    """Simple logger for inheritance only. By default log into console with INFO level"""

    def __init__(self,
                 name: str,
                 console: bool = True,
                 console_level: str = 'INFO',
                 file: bool = False,
                 file_level: str = 'DEBUG',
                 date_format: str = '%Y-%m-%d %H:%M:%S',
                 log_format: str = '%(asctime)-15s [%(name)s] [LINE:%(lineno)d] [%(levelname)s] %(message)s',
                 enabled: bool = True):

        self.name = name
        self.console = console
        self.console_level = console_level
        self.file = file
        self.file_level = file_level
        self.date_format = date_format
        self.log_format = log_format
        self.enabled = enabled

        # Get logger
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter(fmt=self.log_format, datefmt=self.date_format)
        self.logger.disabled = not self.enabled

        # Console handler with a INFO log level
        if self.console:
            # use param stream=sys.stdout for stdout printing
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            ch.setFormatter(self.formatter)  # Add the formatter
            self.logger.addHandler(ch)  # Add the handlers to the logger

        # File handler which logs debug messages
        if self.file:
            fh = logging.FileHandler(f'{self.name}.log', mode='w')
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(self.formatter)  # Add the formatter
            self.logger.addHandler(fh)  # Add the handlers to the logger

    def __call__(self, *args, **kwargs):
        return self.logger

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Enabled: {self.enabled}\n' \
               f'Console logging: {self.console}\n' \
               f'Console level: {self.console_level}\n' \
               f'File logging: {self.file}\n' \
               f'File level: {self.file_level}\n' \
               f'File name: {self.name}.log'
