# coding=utf-8
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tuyaha-float",
    version="0.0.7",
    author="ThePinkOwl (Roger Miret Giné), Pavlo Annekov and original Tuya authors",
    author_email="roger.miret@gmail.com",
    description="A Python library that implements a Tuya API endpoint that was specially designed for Home Assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/thepinkowl/tuyaha-float",
    license="MIT",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
