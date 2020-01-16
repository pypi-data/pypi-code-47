"""
Module Setup
"""
import os
import sys
from distutils.sysconfig import get_python_lib
from setuptools import setup

RELATIVE_SITE_PACKAGES = get_python_lib().split(sys.prefix + os.sep)[1]
DATE_FILES_RELATIVE_PATH = os.path.join(RELATIVE_SITE_PACKAGES, "dora")

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name="dora-isa",
    version="0.2.1.22",
    packages=[
        'dora',
        'dora/interface',
        'dora/template/cp/score',
    ],
    data_files=[
        (DATE_FILES_RELATIVE_PATH + "/template", ['dora/template/Dockerfile']),
        (DATE_FILES_RELATIVE_PATH + "/template/cp/score", ['dora/template/cp/score/run.sh'])
    ],
    author="didone",
    url="http://www.compasso.com.br",
    author_email="tiago.didone@compasso.com.br",
    description="SQL Parser for Dora Project",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
