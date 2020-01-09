"""
Generate an index of documentation pages from multiple sets of docs pages.
"""

from .get_metadata import get_package_metadata

from pathlib import Path

__version__ = "0.1.8"
version = __version__
__all__ = ["get_package_metadata", "static_path"]


def static_path() -> Path:
    return Path(__file__).parent.absolute() / "_static"
