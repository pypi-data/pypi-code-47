#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'canopy-toolkit'
DESCRIPTION = 'Nifty utilities to access Canopy resources via python.'
URL = 'https://github.com/Mesitis/aws-lambdas/utilities/canopy-toolkit'
EMAIL = 'niranjan.rajendran@canopy.cloud'
AUTHOR = 'Niranjan Rajendran'
REQUIRES_PYTHON = '>=3.6.0'

REQUIRED = [
    'hvac', 'requests', 'botocore', 'async-property'
]

EXTRAS = {
    'psycopg2': ['psycopg2-binary'],
    'asyncpg': ['asyncpg', 'asyncio-helpers'],
    'api': ['pyotp', 'requests-toolbelt', 'websockets'],
    'crypto': ['pycryptodomex']
}

all_extras = set()
for dependencies in EXTRAS.values():
    for dependency in dependencies:
        all_extras.add(dependency)

EXTRAS['all'] = list(all_extras)

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
project_slug = NAME.lower().replace('-', '_')
with open(os.path.join(here, project_slug, '__version__.py')) as f:
    exec(f.read(), about)

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
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*', 'tests.*']),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='proprietary',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: Other/Proprietary License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
