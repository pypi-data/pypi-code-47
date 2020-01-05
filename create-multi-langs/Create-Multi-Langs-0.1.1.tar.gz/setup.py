#!/usr/bin/env python

from setuptools import setup, find_packages

description = \
"Create-Multi-Langs is a library for creating code file from translated csv file."  # noqa: E501

with open('requirements.txt') as fid:
    requires = [line.strip() for line in fid]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Create-Multi-Langs',
    version='0.1.1',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Yihua Chiu',
    author_email='mychiux413@gmail.com',
    url="https://github.com/mychiux413/create-multi-langs",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['create-multi-langs=create_multi_langs.command_line:main'],  # noqa: E501
    },
    platforms="any",
    python_requires='>=3.5',
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Code Generators",
        "Typing :: Typed",
    ],
    install_requires=requires,
)
