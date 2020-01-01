from galaxyutils.__init__ import __version__
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="galaxyutils",
    version=__version__,
    author="Tyler Nichols",
    author_email="tylerbrawl@gmail.com",
    description="This module contains utilities that Galaxy 2.0 plugin developers may find useful.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tylerbrawl/Galaxy-Utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities"
    ],
    python_requires=">=3.7"
)
