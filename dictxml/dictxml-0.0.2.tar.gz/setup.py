#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: lijin
# Mail: lijin@dingtalk.com
# Created Time:  2019-12-06
#############################################

from setuptools import setup, find_packages

setup(
    name="dictxml",
    version="0.0.2",
    keywords=("pip", "pathtool", "timetool", "magetool", "mage"),
    description="xml和dict互相转换",
    long_description="xml和dict互相转换",
    license="MIT Licence",

    url="https://github.com/l616769490/dictxml",
    author="lijin",
    author_email="lijin@dingtalk.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[]
)
