# -*- coding: utf-8 -*-

"""
SeleniumTestability
"""
from os.path import abspath, dirname, join
from setuptools import setup

LIBRARY_NAME = "importresource-testdata"
CWD = abspath(dirname(__file__))

# Get the long description from the README file
with open(join(CWD, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

CLASSIFIERS = """
Development Status :: 3 - Alpha
Topic :: Software Development :: Testing
Operating System :: OS Independent
License :: OSI Approved :: Apache Software License
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
""".strip().splitlines()

setup(
    name="robotframework-%s" % LIBRARY_NAME.lower(),
    version="1.0",
    description="Test data package for robotframework-importresource",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rasjani/robotframework-%s" % LIBRARY_NAME.lower(),
    author="Jani Mikkonen",
    author_email="jani.mikkonen@gmail.com",
    license="Apache License 2.0",
    classifiers=CLASSIFIERS,
    keywords="robot framework testing automation selenium seleniumlibrary",
    platforms="any",
    packages=[LIBRARY_NAME],
    package_dir={"": "src"},
    package_data={LIBRARY_NAME: ["rf-resources/*.resource"]},
)
