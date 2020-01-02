"""
Setup
"""
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="python_request_fanout",
    version="1.0.0",
    description="make multiple requests concurrently and get their responses",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Eitol/python_request_fanout",
    author="Hector Oliveros",
    author_email="hector.oliveros.leon@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["python_request_fanout"],
    include_package_data=True,
    install_requires=["requests", 'pytest'],
    entry_points={
        "console_scripts": []
    },
)
