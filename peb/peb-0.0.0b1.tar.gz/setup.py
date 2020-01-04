#!/usr/bin/env python

import os
import sys
from shutil import rmtree

from setuptools import Command, setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
VERSION = '0.0.0b1'


def read(f):
    return open(f, 'r', encoding='utf-8').read()


class UploadCommand(Command):
    """Support setup.py upload."""

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
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
            rmtree(os.path.join(here, 'build'))
            rmtree(os.path.join(here, 'peb.egg-info'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')
        sys.exit()


setup(
    name='peb',
    version=VERSION,
    description='PEB is extensions of python',
    long_description=read('README.rst'),
    long_description_content_type='text/x-rst',
    url='https://github.com/joyongjin/peb',
    author='Yongjin Jo',
    author_email='wnrhd114@gmail.com',
    lisence='MIT',
    packages=find_packages(exclude=['tests*', '.*']),
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
    cmdclass={
        'upload': UploadCommand,
    }
)
