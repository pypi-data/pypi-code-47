from setuptools import setup

# Read the contents of your README file to upload with PyPi package.
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pybsv",
    version="0.0.3",
    description="An easy to use Python BSV client.",
    url="http://github.com/jannainm/pybsv",
    author="jannainm",
    author_email="jannainm@gmail.com",
    license="MIT",
    packages=["pybsv"],
    install_requires=["bitsv<1"],
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown",
)
