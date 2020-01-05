import os
from setuptools import setup, find_packages
from pyferno.util.version import find_version


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="pyferno",
    version=find_version(os.getcwd(), "pyferno/version.py"),
    description="PyFerno - the async/promise library for Python 3 async inferno",
    url="https://github.com/svenvarkel/pyferno",
    author="Sven Varkel",
    author_email="sven@prototypely.com",
    license="MIT",
    packages=find_packages(),
    install_requires=read_requirements(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
