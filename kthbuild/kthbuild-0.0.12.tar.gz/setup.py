#!/usr/bin/env python

# 
# Copyright (c) 2020 Fernando Pelliccioni
# 

from setuptools import setup

__title__ = "kthbuild"
__summary__ = "Knuth node build tools"
__uri__ = "https://github.com/k-nuth/kthbuild"
__version__ = "0.0.12"
__author__ = "Fernando Pelliccioni"
__email__ = "fpelliccioni@gmail.com"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2020 Fernando Pelliccioni"


install_requires = [
    "conan >= 1.21.1",
    "cpuid >= 0.0.6",
]

setup(
    name = __title__,
    version = __version__,
    description = __summary__,
    long_description=open("./README.rst").read(),
    license = __license__,
    url = __uri__,
    author = __author__,
    author_email = __email__,

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],    

    # What does your project relate to?
    keywords='knuth crypto bitcoin btc bch cash build tool',

    py_modules=["kthbuild"],

    install_requires=install_requires,
    # setup_requires=setup_requires,
    

    dependency_links=[
        'https://testpypi.python.org/pypi',
        # 'https://testpypi.python.org/pypi/cpuid-native/',
    ],

    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },
)

