from .core import encode
from .core import decode
from .core import encode as compress
from .core import decode as decompress
from .streams import open
from .streams import HeatshrinkFile
from .streams import HeatshrinkFile as EncodedFile

__all__ = ['encode', 'decode', 'open', 'HeatshrinkFile', 'EncodedFile']
