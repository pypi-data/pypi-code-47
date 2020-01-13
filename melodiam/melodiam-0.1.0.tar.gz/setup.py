#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    """
    with open(os.path.join(package, "__init__.py")) as f:
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", f.read()).group(1)


def get_long_description():
    """
    Return the README.md.
    """
    with open("README.md", encoding="utf8") as f:
        return f.read()


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]


setup(
    name="melodiam",
    python_requires=">=3.6",
    version=get_version("melodiam"),
    url="https://gitlab.com/harry.sky.vortex/melodiam",
    license="MIT License",
    description="Melodiam - async, 100% tested and type-annotated Spotify Web API wrapper.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Igor Nehoroshev",
    author_email="mail@neigor.me",
    packages=get_packages("melodiam"),
    data_files=[("", ["LICENSE"])],
    include_package_data=True,
    install_requires=["httpx"],
    extras_require={
        "lint": ["mypy", "autoflake", "black", "isort"],
        "test": ["asynctest", "starlette", "python-multipart"],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
