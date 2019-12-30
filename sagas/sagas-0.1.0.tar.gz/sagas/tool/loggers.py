import logging.config
import yaml

def init_logger(file='/pi/stack/conf/logger.yml'):
    with open(file, 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

# Usage:
# logger = logging.getLogger(__name__)
#
# logger.debug('This is a debug message')
# msg='hi'
# logger.info(f"{msg}")

