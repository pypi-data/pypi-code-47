import logging
from logging.handlers import RotatingFileHandler
import os
import sys

import panaetius
from panaetius import CONFIG as CONFIG
from panaetius import __header__ as __header__
from panaetius import set_config as set_config


panaetius.set_config(CONFIG, 'logging.path')
panaetius.set_config(
    CONFIG,
    'logging.format',
    '{\n\t"time": "%(asctime)s",\n\t"file_name": "%(filename)s",'
    '\n\t"module": "%(module)s",\n\t"function":"%(funcName)s",\n\t'
    '"line_number": "%(lineno)s",\n\t"logging_level":'
    '"%(levelname)s",\n\t"message": "%(message)s"\n}',
    cast=str,
)
set_config(CONFIG, 'logging.level', 'INFO')

# Logging Configuration
logger = logging.getLogger(__header__)
loghandler_sys = logging.StreamHandler(sys.stdout)

# Checking if log path is set
if CONFIG.logging_path:
    CONFIG.logging_path += (
        f'{__header__}.log'
        if CONFIG.logging_path[-1] == '/'
        else f'/{__header__}.log'
    )
    # Set default log file options
    set_config(CONFIG, 'logging.backup_count', 3, int)
    set_config(CONFIG, 'logging.rotate_bytes', 512000, int)

    # Configure file handler
    loghandler_file = RotatingFileHandler(
        os.path.expanduser(CONFIG.logging_path),
        'a',
        CONFIG.logging_rotate_bytes,
        CONFIG.logging_backup_count,
    )

    # Add to file formatter
    loghandler_file.setFormatter(logging.Formatter(CONFIG.logging_format))
    logger.addHandler(loghandler_file)

# Configure and add to stdout formatter
loghandler_sys.setFormatter(logging.Formatter(CONFIG.logging_format))
logger.addHandler(loghandler_sys)
logger.setLevel(CONFIG.logging_level)
