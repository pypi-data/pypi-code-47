"""
PyTesting utils is a collection of utilities for the PyTesting project.

This file is part of PyTesting utils.

PyTesting utils is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PyTesting utils is distributed in the hope that it will be useful
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with PyTesting utils.  If not, see <https://www.gnu.org/licenses/>.
"""
import contextlib
import os
import shutil
import tempfile
from typing import Union, Generator, Any, Callable

from pytesting_utils.virtual_environment import VirtualEnvironment


# pylint: disable=invalid-name
@contextlib.contextmanager
def cd(
    new_dir: Union[bytes, str, os.PathLike], cleanup: Callable[[], bool] = lambda: True,
) -> Generator[Any, Any, None]:
    """
    A context that changes directories

    :param new_dir: The new directory path
    :param cleanup: A function indicating whether the directory should be
    removed after the context was left
    :return: A generator for the context
    """
    prev_dir: Union[bytes, str] = os.getcwd()
    os.chdir(os.path.expanduser(new_dir))
    try:
        yield
    finally:
        os.chdir(prev_dir)
        cleanup()


@contextlib.contextmanager
def tempdir() -> Generator[Union[bytes, str], Any, None]:
    """
    Creates a context holding a temporary directory

    :return: The context generator
    """
    dir_path = tempfile.mkdtemp()

    def cleanup():
        shutil.rmtree(dir_path)
        return True

    with cd(dir_path, cleanup):
        yield dir_path


@contextlib.contextmanager
def virtualenv(
    env_name: str, tmp_dir: Union[bytes, str, os.PathLike] = None
) -> Generator[VirtualEnvironment, Any, None]:
    """
    Creates a context for a virtual environment.

    It creates a virtual environment in a temporary folder and yields an
    object of the VirtualEnvironment class.

    :param env_name: The name for the virtual environment
    :param tmp_dir: An optional root path for the temporary directory
    :return: A VirtualEnvironment object wrapping the virtual environment
    """
    venv = VirtualEnvironment(env_name, tmp_dir)
    yield venv
    venv.cleanup()
