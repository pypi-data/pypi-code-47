#!/usr/bin/env python
#-*- coding:utf-8 -*-
#############################################
# File Name: setup.py
# Author: yvan
# Mail: 
# Created Time: 2020-1-15
#############################################
from setuptools import setup, find_packages

setup(
    name = "pytooltest",
    version = "0.1.0",
    keywords = ("pip", "pytooltest"),
    description = "pytooltest",
    long_description = "pytooltest",
    license = "MIT Licence",

    url = "https://github.com/yvan233/pipproject",
    author = "yvan",
    author_email = "2624507753@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [])