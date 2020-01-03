import os
from setuptools import setup, find_packages

BASE = os.path.dirname(__file__)
with open(os.path.abspath(os.path.join(BASE, "README.md")), "r") as handler:
      readme = handler.read()

with open(os.path.abspath(os.path.join(BASE, 'requirements.txt')), "r") as handler:
      requires = handler.read().splitlines()

setup(
    name='pyini',
    install_requires=requires,
    version="0.1.0",
    description="INI configuration file parser with useful standard extensions.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Kieran Bacon",
    author_email="Kieran.Bacon@outlook.com",
    url="https://github.com/Kieran-Bacon/pyini",
    packages=find_packages(),
    classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License"
    ]
)