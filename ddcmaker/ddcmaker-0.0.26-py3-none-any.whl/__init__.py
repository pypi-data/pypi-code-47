__version__ = '0.0.26'
__metaclass__ = type
__all__ = [
    '__init__', 'car', 'arm', 'dog', 'human', 'spider'
]
NAME = 'ddcmaker'

import platform

if platform.system() == "Linux":
    from ddcmaker.linux.armv7l.maker import *
else:
    from ddcmaker.confusion.maker import *
