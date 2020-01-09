# -*- coding=utf-8 -*-

import os
from setuptools import setup

def raw_read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), 'r') as f:
        return f.read()

try:
    from pypandoc import convert_text
    read = lambda fname: convert_text(raw_read(fname), 'rst', format='md')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read = raw_read

setup(
    name='taza',
    version='1.2.1',
    author='Daniel Domínguez',
    author_email='daniel.dominguez@imdea.org',
    description= ('A set of classes and abstractions for working with Tacyt'),
    license='MIT',
    keywords='mobile tacyt android',
    url = 'https://gitlab.software.imdea.org/android/taza',
    packages = ['taza', 'taza/tacyt', 'taza/tacyt/authorization'],
    long_description = read('README.md'),
)

