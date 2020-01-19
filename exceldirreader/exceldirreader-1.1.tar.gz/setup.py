import setuptools
from pathlib import Path


setuptools.setup(
    name="exceldirreader",
    version=1.1,
    description="Reads multiple excel files from a directory",
    long_description=Path("README.md").read_text(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(exclude=["tests", "data"])
)