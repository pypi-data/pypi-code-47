#!/usr/bin/env python

import setuptools


INSTALL_REQUIRES = [
    'numpy >= 1.14.3',
    'matplotlib >= 2.2.2',
    'mako ==1.0.12',
    'pandas >= 0.24.2',
    'scikit-learn >= 0.20.2',
    'pytest >= 4.6.2',
    'python-dateutil >= 2.7.3',
    'setuptools >= 39.1.0'
]



setuptools.setup(
    name='ds4mllib',
    description='A python library for data synthesis and evaluation',
    version='0.0.2',
    packages=setuptools.find_packages(),
    author=['Rongjun', 'Yan', 'David'],
    author_email= 'yan.zhao01@sap.com',
    install_requires=INSTALL_REQUIRES,
    platform='any'
)

