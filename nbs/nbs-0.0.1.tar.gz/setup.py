#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : setup.py
# Author            : JCHRYS <jchrys@me.com>
# Date              : 06.01.2020
# Last Modified Date: 06.01.2020
# Last Modified By  : JCHRYS <jchrys@me.com>
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
        name="nbs", 
        version="0.0.1", 
        packages= find_packages(),
        description="Book information crawler using 'NAVER BOOKS API'",
        author="JCHRYS",
        author_email="jchrys@me.com",
        long_description=long_description,
        url='https://github.com/jchrys/NBCrawler',
        install_requires=["requests",
            "bs4", 
            "tqdm",
            ],
        python_requires='>=3.6',
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            ]
        )
