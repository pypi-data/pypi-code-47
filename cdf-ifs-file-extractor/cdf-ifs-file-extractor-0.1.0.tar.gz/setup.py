import re

from setuptools import find_packages, setup

version = re.search(r'^__version__\s*=\s*"(.*)"', open("cdf_ifs_file_extractor/_version.py").read(), re.M).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cdf-ifs-file-extractor",
    version=version,
    author="Cognite",
    author_email="jonas.mack@cognite.com",
    description="Python package for extracting files from IFS to CDF. Copyright 2020 Cognite AS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "cognite-sdk>=1.1.0",
        "google-cloud-logging>=1.12.1",
        "cognite-prometheus>=0.1.0",
        "pyyaml>=5.1.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
    ],
    python_requires=">=3.5",
)
