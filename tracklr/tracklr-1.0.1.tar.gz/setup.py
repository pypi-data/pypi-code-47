#!/usr/bin/env python

PROJECT = "tracklr"

from tracklr import Tracklr

VERSION = Tracklr.__version__


from setuptools import setup, find_packages

try:
    long_description = open("README.rst", "rt").read()
except IOError:
    long_description = ""

setup(
    name=PROJECT,
    version=VERSION,
    description="Tracklr - Command-line Productivity Toolset",
    long_description=long_description,
    author="Marek Kuziel",
    author_email="marek@kuziel.info",
    url="https://gitlab.com/markuz/tracklr",
    download_url="https://gitlab.com/markuz/tracklr/-/archive/master/tracklr-master.tar.bz2",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Environment :: Console",
    ],
    platforms=["Any"],
    scripts=[],
    provides=[],
    install_requires=[
        "cliff",
        "appdirs",
        "icalendar",
        "jinja2",
        "pyyaml",
        "requests",
        "xhtml2pdf",
        "khal",
    ],
    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": ["tracklr = tracklr.main:main"],
        "tracklr": [
            "ls = tracklr.ls:Ls",
            "tag = tracklr.tag:Tag",
            "pdf = tracklr.pdf:Pdf",
            "init = tracklr.init:Init",
            "show = tracklr.show:Show",
        ],
    },
    zip_safe=False,
)
