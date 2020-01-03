try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from ctfcli import __version__
import os

setup(
    name="ctfcli",
    version=__version__,
    author="",
    license="MIT",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    keywords=["ctfcli"],
    classifiers=[],
    packages=["ctfcli"],
    include_package_data=True,
)
