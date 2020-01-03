#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 18:41:58 2020

@author: charlie
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="google-word-cloud-Chaz9578", # Replace with your own username
    version="0.0.1",
    author="Charlie Plumley",
    author_email="charlie.plumley@gmail.com",
    description="Create word clouds from a google search term",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/charlie9578/googleWordCloud",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)