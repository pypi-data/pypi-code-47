#!/usr/bin/env python3
from setuptools import setup, find_namespace_packages

test_packages = ["pytest", "mock"]

setup(
    name='vcap.utils',
    version='0.0.3-alpha',
    description="Utilities for creating OpenVisionCapsules easily in Python",
    packages=find_namespace_packages(include=['vcap.*']),
    namespace_packages=['vcap'],

    author="Dilili Labs",

    install_requires=[
        "vcap"
    ],

    extras_require={
        "tests": test_packages,
    },
    tests_require=test_packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
