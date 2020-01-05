from .core import encode
from .core import decode
from .core import encode as compress
from .core import decode as decompress
from .streams import open
from .streams import HeatshrinkFile
from .streams import HeatshrinkFile as EncodedFile
from .version import __version__

__all__ = [
    'compress',
    'decompress',
    'open',
    'HeatshrinkFile',
    '__version__'
]
