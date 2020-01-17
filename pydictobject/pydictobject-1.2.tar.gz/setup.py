"""Setup file for dictobject"""

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pydictobject',
    version='v1.02',
    description='pydictobject - a dictionary that is accessible like an object',
    packages=['pydictobject'],
    author='Peter Harris',
    author_email='pdrharris@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/pdrharris/pydictobject',
    download_url='https://github.com/pdrharris/pydictobject/archive/1.02.tar.gz',
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
