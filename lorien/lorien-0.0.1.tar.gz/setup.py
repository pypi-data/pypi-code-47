"""Package Setup"""
import os
from distutils.core import setup

from setuptools import find_packages

CURRENT_DIR = os.path.dirname(__file__)

def read(path):
    with open(path, "r") as filep:
        return filep.read()

setup(
    name="lorien",
    version="0.0.1",
    license="Apache-2.0",
    description="A Hyper-Automated Tuning System for Tensor Operators",
    long_description=read(os.path.join(CURRENT_DIR, 'README.md')),
    long_description_content_type='text/markdown',
    author="Cody Yu",
    author_email="comaniac0422@gmail.com",
    url="https://github.com/comaniac/lorien",
    keywords=[],
    packages=find_packages(),
    install_requires=[
        "setuptools", "future", "tqdm > 4.40", "argparse", "rpyc", "gitpython", "boto3", "pyyaml"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
