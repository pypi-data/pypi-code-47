from setuptools import setup
import os

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="py_matching_pattern",
    description="Dynamic Pattern Matching Library",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    version="0.0.3",
    packages=["py_matching_pattern"],
    url='https://github.com/diogok/py_matching_pattern',
)
