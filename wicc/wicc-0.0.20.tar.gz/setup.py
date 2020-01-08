#!/usr/bin/python
# -*- coding: utf-8 -*-
import setuptools
import io

with io.open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    # name="waykichain",
    name="wicc",
    version="0.0.20",
    author="louis han",
    author_email="louishwh@gmail.com",
    description="WaykiChain Wallet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/louishwh/",
    packages=setuptools.find_packages(),
    install_requires=[
        'cryptos',
        'requests',
        'pbkdf2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


# python -m twine upload dist/