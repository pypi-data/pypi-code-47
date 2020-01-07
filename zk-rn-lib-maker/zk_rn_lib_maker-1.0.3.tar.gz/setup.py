#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: JeffreyCao
# Mail: jeffreycao1024@gmail.com
# Created Time:  2019-11-16 21:48:34
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#package-data
#############################################

# from setuptools import setup, find_packages  # 这个包没有的可以pip一下
import setuptools
import ezutils.files
import os


def brother_path(file_name):
    return os.path.join(os.path.abspath(
        os.path.dirname(__file__)), file_name)


version_str = ezutils.files.readstr(
    brother_path('zk_rn_lib_maker/version.cfg'))

setuptools.setup(
    name="zk_rn_lib_maker",
    version=version_str,
    keywords=("pip", "zk_rn_lib_maker"),
    description="Tool to create react-native lib for zhike",
    long_description="Tool to create react-native lib for zhike",
    license="MIT Licence",

    url="https://gitee.com/smartstudy/zk_rn_lib_maker.git",
    author="JeffreyCao",
    author_email="jeffreycao1024@gmail.com",

    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        'zk_rn_lib_maker': ['version.cfg'],
    },
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'zk-rn-lib-maker = zk_rn_lib_maker.__main__:main'
        ]
    }
)
