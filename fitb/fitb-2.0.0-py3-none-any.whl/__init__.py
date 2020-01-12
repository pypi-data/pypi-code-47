"""A practical configuration system.
"""

from .extension_point import ExtensionPoint  # noqa: F401
from .loading import load_from_pkg_resources  # noqa: F401
from .option import Option  # noqa: F401
from .utilities import default_config, merge  # noqa: F401
