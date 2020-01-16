#!/usr/bin/env python

from setuptools import setup

setup(
    setup_requires=['pbr'],
    install_requires=['django-model-utils>=2.0', 'django-appconf', 'Django>=2.0<3.0'],
    pbr=True
)
