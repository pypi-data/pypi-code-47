#!/usr/bin/env python3
#
# Copyright (C) 2019-2020 Cochise Ruhulessin
#
# This file is part of unimatrix.ext.vault.
#
# unimatrix.ext.vault is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# unimatrix.ext.vault is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with unimatrix.ext.vault.  If not, see <https://www.gnu.org/licenses/>.
import os.path
from setuptools import find_namespace_packages
from setuptools import setup


curdir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(curdir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='unimatrix.ext.vault',
    version='0.1.0',
    description='Unimatrix One Vault subsystem client library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Cochise Ruhulessin',
    author_email='cochise.ruhulessin@digitalcitizen.nl',
    url='https://gitlab.com/unimatrixone/libraries/python-unimatrix/vault',
    install_requires=[
        "unimatrix>=0.1.5",
        "requests",
        "python-ioc",
    ],
    packages=find_namespace_packages(),
    include_package_data=True,
    license="GPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Clustering",
        "Topic :: System :: Distributed Computing"
    ]
)
