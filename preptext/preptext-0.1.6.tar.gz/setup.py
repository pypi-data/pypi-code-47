#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import io
import re
from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(os.path.join(os.path.dirname(__file__), *names),
                 encoding=kwargs.get("encoding", "utf8")) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


VERSION = find_version('preptext', '__init__.py')

setup_info = dict(
    # Metadata
    name='preptext',
    version=VERSION,
    author='Cunliang Kong',
    author_email='cunliang.kong@outlook.com',
    url='https://github.com/styxjedi/preptext',
    description='Utilities for preprocessing texts',
    license='BSD',
    install_requires=['tqdm', 'numpy', 'six'],

    # Package info
    packages=find_packages(),
    zip_safe=True,
)

setup(**setup_info)
