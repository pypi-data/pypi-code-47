from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name="topsis-401703007",
	version='0.0.1',
	author='Ekjot Singh',
	author_email='esingh_bemba17@thapar.edu',
	description='topsis package implementation',
	long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.python.org/pypi/topsis-401703007",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
	)