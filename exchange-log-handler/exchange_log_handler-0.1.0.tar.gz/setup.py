#!/usr/bin/env python3
# coding: utf-8
'''
Author: Park Lam <lqmonline@gmail.com>
'''

import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

with open('VERSION', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name='exchange_log_handler',
    # TODO: sync version with Chrome Driver
    version=version,
    author='Park Lam',
    author_email='lqmonline@gmail.com',
    description='Log handler to send log via exchange.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/parklam/exchange_log_handler',
    #packages=setuptools.find_packages(),
    packages=['exchange_log_handler'],
    include_package_data=True,
    license='Apache License 2.0',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'exchangelib==2.1.1',
    ],
    keywords='log handler exchange',
)
