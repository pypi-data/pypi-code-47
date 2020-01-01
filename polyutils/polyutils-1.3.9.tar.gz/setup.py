"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='polyutils',
    version='1.3.9',
    packages=['polyutils'],
    url='https://github.com/gstfrr/polyutils',
    download_url='https://github.com/gstfrr/polyutils/archive/v1.3.9.tar.gz',
    license='MIT',
    author='Augusto Ferreira',
    author_email='gstfrr@gmail.com',
    description='This package contains some useful functions for 3D cutting and packing problems '
                'like a 3D Visualizer, placement rules for objects etc...',
    install_requires=[
        'numpy',
        'mayavi',
        'pyvoro',
        'wxPython',
        'PyQt5',
        'scipy',
    ]
)
