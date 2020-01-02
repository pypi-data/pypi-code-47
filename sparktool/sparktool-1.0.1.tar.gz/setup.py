'''
@Date: 2019-12-08 01:59:23
@LastEditors  : ryan.ren
@LastEditTime : 2020-01-02 23:25:55
@Description: 
'''
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sparktool",
    version="1.0.1",
    author="ryanren",
    author_email="strrenyumm@gmail.com",
    description="sparktool for hccn",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/renyumm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
