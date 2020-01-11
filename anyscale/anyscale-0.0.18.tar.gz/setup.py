from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re

from setuptools import setup, find_packages


def find_version(path):
    with open(path) as f:
        match = re.search(
            r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.MULTILINE)
        if match:
            return match.group(1)
        raise RuntimeError("Unable to find version string.")


setup(
    name="anyscale",
    version=find_version("anyscale/__init__.py"),
    author="Anyscale Inc.",
    description=("Command Line Interface for Anyscale"),
    packages=find_packages(),
    setup_requires=['setuptools_scm'],
    install_requires=[
        "boto3", "Click>=7.0", "GitPython", "jsonschema", "ray",
        "requests", "tabulate", "tqdm"
    ],
    entry_points={
        "console_scripts": [
            "anyscale=anyscale.scripts:main"
        ]
    },
    include_package_data=True,
    zip_safe=False)
