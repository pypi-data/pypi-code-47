#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Adapted from https://github.com/navdeep-G/setup.py

import io
import os
from setuptools import find_packages, setup

# Basic module information.
NAME = 'py_GB_tracks'
DESCRIPTION = 'This package implements functions to generate a GenomBrowser trackhub from WGA analyses data'
URL = ''
EMAIL = 'romain.feron.91@gmail.com'
AUTHOR = 'Romain Feron'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'

# Required packages for this module (list package names)
REQUIRED = [
]

# Optional packages for this module (dictionary: 'feature name': ['package name'])
EXTRAS = {
}

# Path to this setup.py file
here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except os.FileNotFoundError:
    long_description = DESCRIPTION  # If there is no README.md file, the provided description is used

# If VERSION was not specified, try to get the version number from __version__.py
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

# Core part of setup.py, build package from all the provided information
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    dependency_links=[],
    extras_require=EXTRAS,
    include_package_data=True,
    license='GPLv3',
    classifiers=[
        # Trove classifiers for pypi (equivalent of tags)
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)
