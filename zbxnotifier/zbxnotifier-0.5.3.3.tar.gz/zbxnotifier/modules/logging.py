import logging
from zbxnotifier.modules.settings import Settings


class Logging:
    @staticmethod
    def init():
        logger = logging.getLogger('basic')
        logger.setLevel(logging.INFO)

        fh = logging.FileHandler(Settings.logfile_path)
        fh.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    @staticmethod
    def change_level(str_level):
        logger = logging.getLogger('basic')
        level = logging.getLevelName(str_level)

        logger.info("Setting loglevel to: " + str(str_level))
        logger.setLevel(level)