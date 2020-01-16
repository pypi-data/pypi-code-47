import os
import json
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as f:
    README = f.read()

setup(
    name="watched-schema",
    version="0.0.16",
    description="WATCHED.com JSON Schema",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/watchedcom/schema",
    author="WATCHED",
    author_email="dev@watched.com",
    packages=find_packages(),
    install_requires=["pyyaml", "jsonschema"],
    package_data={"": ["schema.yaml"]},
    python_requires=">=3.4",
)
