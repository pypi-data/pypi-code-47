#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name = "vimo-utils",
    version = "0.0.1.dev1",
    packages = find_packages(),
    author = "Wizard Li",
    author_email = "lsw1991abc@gmail.com",
    url = "https://github.com/lsw1991abc/py-vimo-utils",
    long_description = read('README.md'),
    long_description_content_type = "text/markdown",
    include_package_data = True
)
