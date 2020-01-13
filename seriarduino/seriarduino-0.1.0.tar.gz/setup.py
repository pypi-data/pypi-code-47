#!/usr/bin/env python

from setuptools import setup

with open("../README.md", "r") as fh:
    long_description = fh.read()

setup(name='seriarduino',
      version='0.1.0',
      description='[BETA] Link Arduino and Python using serial port',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Norech',
      author_email='alexis.norech@gmail.com',
      url='https://github.com/norech/SeriArduino',
      packages=['seriarduino'],
      install_requires=[
          'pyserial',
      ]
     )