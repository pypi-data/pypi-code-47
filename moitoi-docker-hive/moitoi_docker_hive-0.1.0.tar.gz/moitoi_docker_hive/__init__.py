"""Top-level package for MoiToi Docker Hive."""

__author__ = """Andres Kepler"""
__email__ = 'andres@kepler.ee'
__version__ = '0.1.0'

import logging.config
import uuid
from os.path import expanduser

DEFAULT_CONFIG_DIR = expanduser("~") + "/.mdh"
DEFAULT_CONFIG_FILE = DEFAULT_CONFIG_DIR + "/mdh.yaml"
DEFAULT_MDH_PASSWORD = "Change;Me"
DEFAULT_MDH_CLUSTER_ID = "mdh" + str(uuid.uuid1()).replace("-", "")
DEFAULT_MDH_LD_PORT = 5000
DEFAULT_MDH_BACKEND_PORT = 5000

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d %(funcName)s - %(message)s'
        },
    },
    'handlers': {
        'log': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        '': {
            'handlers': ['log'],
            'level': 'INFO',
        }
    }
})

DEFAULT_CONFIG = [{
    "provider": {
        "name": "local",
        "dockerhost": "localhost"
    },
},
    {"password": DEFAULT_MDH_PASSWORD},
    {"backend_port": DEFAULT_MDH_BACKEND_PORT}

]
