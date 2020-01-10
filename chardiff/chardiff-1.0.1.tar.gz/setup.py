#!/usr/bin/env python

from distutils.core import setup

setup(
    name='chardiff',
    version='1.0.1',
    description='Compare 2 strings and highlight differences',
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Matt Copperwaite',
    author_email='matt@copperwaite.net',
    url='https://github.com/yamatt/python3-chardiff',
    packages=['chardiff'],
    scripts=['scripts/chardiff']
)
