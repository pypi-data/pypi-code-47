from typing import List, TextIO

import os
from pathlib import Path

from sys import stdout, stderr

from izitest.prettyprint import (prettyprint, Color)

__all__ = [
    "check_file",
    "check_exec",
    "check_dir"
]


def check_file(path: Path) -> None:
    """Check if given path points to a regular file.

    Args:
        path (Path): path to check

    Raises:
        Exception: if not a regular file
    """
    if not path.is_file():
        prettyprint(f"{path} is not a valid file!", Color.RED, out=stderr)
        raise Exception


def check_exec(path: Path) -> None:
    """Check if given path points to a regular file.

    Args:
        path (Path): path to check

    Raises:
        Exception: if not a regular file
    """
    if not os.access(path, os.X_OK):
        prettyprint(f"{path} is not executable!", Color.RED, out=stderr)
        raise Exception


def check_dir(path: Path) -> None:
    """Check if given path points to a regular file.

    Args:
        path (Path): path to check

    Raises:
        Exception: if not a regular file
    """
    if not path.is_dir():
        prettyprint(f"{path} is not a valid directory!", Color.RED, out=stderr)
        raise Exception
