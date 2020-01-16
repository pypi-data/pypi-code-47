from setuptools import setup, find_packages
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

version = '1.2.5'

setup(
    name='mms-python-adapter',
    version=version,
    description='MMS Communication',
    author='Tanner J Rosenberg, Lenard Halim',
    author_email='Tanner.J.Rosenberg@jpl.nasa.gov, lenard.j.halim@jpl.nasa.gov',
    url='https://github.com/Open-MBEE/MMS-Python-Adapter',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["test", "tests"]),
    install_requires=[
        'mms-python-client<4'
    ],
    license="Apache 2.0",
    classifiers=(
        "Programming Language :: Python :: 3",
    )
)