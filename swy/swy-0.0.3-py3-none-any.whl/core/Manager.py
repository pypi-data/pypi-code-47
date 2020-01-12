import logging
import swy.config.settings
from swy.core import AdbInterface

logger = logging.getLogger('manager')


class Manager:
    """
    This class manages the whole application.
    """

    def __init__(self, settings=swy.config.settings):
        logger.info('Initialising SWY with temporary folder {}'.format(settings.TEMPDIR))
        self.settings = settings
        self.phone = AdbInterface(self.settings.TEMPDIR)

    def run(self):
        logger.debug('Running SWY app')
        self.phone.post_init()  # find a cleaner way to do (separated this to allow cleaning of files and errors raisin)

    def quit(self):
        self.phone.quit()
        logger.debug('Quitting SWY app')
