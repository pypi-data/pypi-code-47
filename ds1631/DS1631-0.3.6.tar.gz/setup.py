#!/usr/bin/python
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='DS1631',
    version='0.3.6',
    py_modules=['DS1631'],
    description='Raspberry pi i2c interface for Maxim-Dallas DS1621 \
DS1631 DS1631A DS1721 DS1731 digital thermometer and thermostat.',
    author='Fabrice Sincère',
    author_email='fabrice.sincere@wanadoo.fr',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GNU General Public License v3.0',
    python_requires='>=3')
