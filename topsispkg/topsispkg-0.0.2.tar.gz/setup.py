# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 19:09:01 2020

@author: Home
"""

import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsispkg", # Replace with your own username
    version="0.0.2",
    author="Priyanshu Gupta",
    author_email="priyanshugupta1904@gmail.com.com",
    description="UCS633/psrana:This package will rank your input on the basis of topsis",
    url="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)