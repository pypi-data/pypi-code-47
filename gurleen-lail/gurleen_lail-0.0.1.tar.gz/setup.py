# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:35:33 2020

@author: DELL
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gurleen_lail", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="gurleen799lail@gmail.com",
    description="It is a self created package for TOPSIS",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
