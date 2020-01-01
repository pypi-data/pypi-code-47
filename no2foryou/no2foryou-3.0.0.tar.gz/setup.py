#!/usr/bin/env python3
import os
import pathlib

import setuptools


def _build_console_scripts():
    return [
        f'{name}=no2foryou:main'
        for name in _executables_in_path()
        if name.startswith(('python2', 'pip2'))
    ]


def _executables_in_path():
    executables = set()
    for directory in os.get_exec_path():
        root = pathlib.Path(directory)
        if root.is_dir():
            for path in root.iterdir():
                try:
                    if path.is_file() and os.access(path, os.X_OK):
                        executables.add(path.name)
                except PermissionError:
                    pass
    return executables


setuptools.setup(
    name='no2foryou',
    version='3.0.0',
    license='WTFPL',
    description='Replaces your Python 2 commands with error messages',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Andrew Rabert',
    author_email='ar@nullsum.net',
    url='https://github.com/nvllsvm/python-no2foryou',
    py_modules=['no2foryou'],
    entry_points={'console_scripts': _build_console_scripts()},
    python_requires='>=3.6'
)
