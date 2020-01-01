# -*- coding: utf-8 -*-
from os.path import abspath, dirname, join
from setuptools import setup, find_packages


setup(
    name="robotframework-corerpahive",
    version="1.1.1",
    description="CoreRPAHive is a Robotic Process Automation library that allow the developer create RPA script easier and reduce complexity under robot script layer.",
    license="Apache License 2.0",
    author="Atthaboon Sanurt",
    url='https://github.com/qahive/robotframework-CoreRPAHive',
    long_description="QAHive RPA library",
    classifiers=[
        "Programming Language :: Python :: 3.6"
    ],
    keywords='robotframework testing automation rpa qahive',
    platforms='any',
    packages=find_packages(),
    install_requires=[
        'inject==3.3.2',
        'openpyxl==2.6.2',
        'setuptools==41.0.1',
        'Pillow==6.2.1',
        'robotframework-seleniumlibrary',
    ],
    test_suite='nose.collector',
    tests_require=['nose', 'parameterized'],
    zip_safe=False,
)
