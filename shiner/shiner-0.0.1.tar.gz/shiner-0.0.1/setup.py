#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from setuptools import setup


DESCRIPTION = 'Shiner makes servers shine'
URL = 'https://gitlab.com/mintlab/devops/ansible/shiner'
EMAIL = 'ops@mintlab.nl'
AUTHOR = 'Flip Hess'
REQUIRES_PYTHON = '>=3.6'
VERSION = '0.0.1'
REQUIRED = [
    "ansible==2.9.2",
]

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='shiner',
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    url=URL,
    license='MIT',
    packages=[
    ],
    include_package_data=True,
    entry_points=dict(console_scripts=[
    ]),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
