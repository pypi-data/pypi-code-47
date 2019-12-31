#!/usr/bin/env python
import sys

from webauthin import __version__

assert sys.version >= "3.6", "Requires Python v2.7 or above."
from setuptools import setup, find_packages  # noqa

setup(
    name="django-webauthin",
    version=__version__,
    author="Stavros Korokithakis",
    author_email="hi@stavros.io",
    url="https://gitlab.com/stavros/django-webauthin",
    description="""Passwordless authentication using WebAuthn.""",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="BSD",
    keywords="django",
    zip_safe=False,
    include_package_data=True,
    install_requires=["py-webauthn-temporary-package"],
    packages=find_packages(),
    python_requires=">=3.6",
)
