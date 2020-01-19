#!/usr/bin/env python

import os
import sys

from setuptools import setup
from setuptools.command.install import install

VERSION = "0.1.0"

def readme():
    """ print long description """
    with open('README.md') as f:
        long_descrip = f.read()
    return long_descrip

class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)

setup(
    name = 'pywand',
    packages = ['pywand'],
    version = VERSION,
    description = 'Read IR codes from MagiQuest Wands',
    long_description=readme(),
    long_description_content_type="text/markdown",
    author = 'Ryan Veach',
    author_email = 'rveach@gmail.com',
    license="MIT",
    url = 'https://gitlab.com/rveach/wand',
    download_url = 'https://gitlab.com/rveach/wand/-/archive/master/wand-master.tar.gz',
    keywords = ['wand', "magiquest", "IR"],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[],
    scripts=[
        'scripts/wands_print_code.py',
        'scripts/wands_print_name.py',
    ],
    python_requires='>=3.5',
    cmdclass={
        'verify': VerifyVersionCommand,
    },
)
