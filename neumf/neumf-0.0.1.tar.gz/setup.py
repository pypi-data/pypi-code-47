import setuptools
from neumf import (
    __name__, __version__,
    __author__,  __author_email__
)

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name    = __name__,
    version = __version__,
    author  = __author__,
    author_email = __author_email__,
    description  = "neumf module",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://pypi.org/project/{}/".format(__name__),
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
