
from .metadata import get_package_version
from .logger import get_logger


__version__ = get_package_version(path=__file__, package_name='sdsstools')

NAME = 'sdsstools'


# Get a logger, mostly for the nice colouring.
log = get_logger(NAME)


from .configuration import *
from .logger import *
from .metadata import *
