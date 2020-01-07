#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""shell history analysis."""

# Third party
from setuptools import setup

requires_all = ["click", "python-dateutil", "matplotlib", "pandas", "pyaml"]
requires_tests = [
    "pytest",
    "pytest-cov",
    "pytest-mccabe",
    "pytest-flake8",
    "simplejson",
]

setup(
    package_data={"shell_history_analysis": ["grouping.yaml"]},
    tests_require=requires_tests,
)
