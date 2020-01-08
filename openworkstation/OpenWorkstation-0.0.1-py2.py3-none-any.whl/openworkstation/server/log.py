import logging
from logging.config import dictConfig
import os
from workstation import util

LOG_FILE_DIR = util.environment.get_path('LOG_DIR')

logging_config = dict(
    version=1,
    formatters={
        'basic': {
            'format': '%(asctime)s %(name)s %(levelname)s [Line %(lineno)s]     %(message)s'  #NOQA
        }
    },
    handlers={
        'debug': {
            'class': 'logging.StreamHandler',
            'formatter': 'basic',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'workstation-app': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'basic',
            'filename': os.path.join(LOG_FILE_DIR, 'workstation-app.log'),
            'maxBytes': 5000000,
            'backupCount': 3
        },
        'socketio': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'basic',
            'filename': os.path.join(LOG_FILE_DIR, 'socketio.log'),
            'maxBytes': 5000000,
            'backupCount': 3
        },
        'workstation': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'basic',
            'filename': os.path.join(LOG_FILE_DIR, 'workstation.log'),
            'maxBytes': 5000000,
            'backupCount': 3
        },
    },
    loggers={
        'workstation-app': {
            'handlers': ['workstation-app'],
            'level': logging.DEBUG,
        },
        # 'socketio': {
        #  'handlers': ['socketio'],
        #  'level': logging.INFO,
        # },
        'workstation': {
            'handlers': ['workstation'],
            'level': logging.DEBUG,
        },
    },
    # Used to override root logger in workstation-api
    root={
        'handlers': ['workstation-app'],
        'level': logging.ERROR,
    }
)

dictConfig(logging_config)
