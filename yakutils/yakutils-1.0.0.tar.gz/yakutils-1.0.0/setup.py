#!/usr/bin/env ython
# -*- coding: utf-8 -*-
"""This module contains setup instructions for yakutils."""
import codecs
import os
import sys
from shutil import rmtree

from setuptools import Command
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()


class UploadCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds ...')
            rmtree(os.path.join(here, 'dist'))
        except Exception:
            pass
        self.status('Building Source distribution ...')
        os.system('{0} setup.py sdist'.format(sys.executable))
        self.status('Uploading the package to PyPI via Twine ...')
        os.system('twine upload dist/*')
        sys.exit()


setup(
    name='yakutils',
    version='1.0.0',
    author='Nick Ficano',
    author_email='nficano@gmail.com',
    packages=['yakutils'],
    url='https://github.com/nficano/yakutils',
    license='MIT',
    package_data={
        '': ['LICENSE'],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    description=(
        'A really lazy package'
    ),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=long_description,
    zip_safe=True,
    cmdclass={'upload': UploadCommand},
)
