#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name='Utils-Config',
    version='1.0.0',
    use_scm_version=False,
    setup_requires=["setuptools_scm"],
    description='Library to use .json files as configuration objects using namedtuple.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Juan Biondi',
    author_email='juanernestobiondi@gmail.com',
    python_requires='>=3.5.0',
    url='https://github.com/yeyeto2788/Utils-Config',
    packages=['utils_config'],
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
