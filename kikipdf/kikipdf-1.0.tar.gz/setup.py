import setuptools
from pathlib import Path

setuptools.setup(
    name="kikipdf",
    version=1.0,
    longe_description=Path("README.md").read_text,
    packages=setuptools.find_packages(exclude=["tests", "data"])
)