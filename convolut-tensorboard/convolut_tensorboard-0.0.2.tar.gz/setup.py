# -*- coding: utf-8 -*-
import io

from setuptools import setup, find_packages

with io.open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

version = "0.0.2"

setup(
    name="convolut_tensorboard",
    version=version,
    description="Tensorboard integrations for convolut framework",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Andrey Avdeev",
    author_email="seorazer@gmail.com",
    license="Apache 2.0",
    packages=find_packages(),
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        "convolut>=0.0.4",
        "tensorboard>=2.1.0"
    ],
    keywords="convolut tensorboard",
    url="https://github.com/convolut/convolut-tensorboard",
)
