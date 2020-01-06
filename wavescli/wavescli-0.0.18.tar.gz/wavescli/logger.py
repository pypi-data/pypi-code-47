import logging


WAVES_LOGGER_CONFIG = {
    'version': 1,
    'handlers': {
        'default': {
            'level': logging.INFO,
            'formatter': 'standard',
            'class': 'logging.StreamHandler'
        },
        'waves': {
            'level': logging.INFO,
            'formatter': 'waves',
            'class': 'logging.StreamHandler'
        }
    },
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] [id:no-identifier] [{}] %(name)s: %(message)s'.format('waves')
        },
        'waves': {
            'format': '%(asctime)s [%(levelname)s] [id:%(identifier)s] [{}] %(name)s: %(message)s'.format('waves')
        }
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': logging.INFO,
            'propagate': True
        },
        'waves': {
            'handlers': ['waves'],
            'level': logging.INFO,
            'propagate': False
        }
    }
}