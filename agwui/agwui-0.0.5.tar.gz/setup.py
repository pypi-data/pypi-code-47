from __future__ import absolute_import
from __future__ import unicode_literals
import os

from setuptools import setup, find_packages
import agwui

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''

def _requires_from_file(filename):
    return open(filename).read().splitlines()

# version
here = os.path.dirname(os.path.abspath(__file__))
version = agwui.__version__

setup(
    name="agwui",
    version=version,
    packages=['agwui'],
    package_dir={'agwui': 'agwui'},
    package_data={'agwui': ['templates/*.html']},
    url='https://github.com/kotauchisunsun/agwui',
    author='kotauchisunsun',
    author_email='kotauchisunshine@hotmail.co.jp',
    maintainer='kotauchisunsun',
    maintainer_email='kotauchisunshine@hotmail.co.jp',
    description='agwui is a library for Automatically Generating Web User Interface for any Python object.',
    long_description=readme,
    install_requires=_requires_from_file('requirements.txt'),
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
    ]
)