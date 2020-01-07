#!/usr/bin/env python3

import re
import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 6, 0, 'final', 0):
    raise SystemExit('Python 3.6 or later is required!')

with open('README.rst', encoding='utf-8') as fd:
    long_description = fd.read()

with open('wulffpack/__init__.py') as fd:
    lines = '\n'.join(fd.readlines())

author_list = ['J. Magnus Rahm',
               'Paul Erhart']
authors = ', '.join(author_list)

version = re.search("__version__ = '(.*)'", lines).group(1)
maintainer = re.search("__maintainer__ = '(.*)'", lines).group(1)
email = re.search("__email__ = '(.*)'", lines).group(1)
description = re.search("__description__ = '(.*)'", lines).group(1)
url = re.search("__url__ = '(.*)'", lines).group(1)
license = re.search("__license__ = '(.*)'", lines).group(1)

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: {}'.format(license),
    'Topic :: Scientific/Engineering :: Physics']


setup(
    name='wulffpack',
    version=version,
    author=authors,
    author_email=email,
    description=description,
    long_description=long_description,
    install_requires=['ase',
                      'numpy>=1.12',
                      'scipy>=0.12.0',
                      'spglib',
                      'matplotlib'],
    packages=find_packages(),
    classifiers=classifiers,
    license=license,
    url=url,
)
