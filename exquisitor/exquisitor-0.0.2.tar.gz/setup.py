import setuptools
#
# Copyright (C) 2015-2019 David J. Beal, All Rights Reserved
#

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="exquisitor",
    version="0.0.2",
    author="David J. Beal",
    author_email="david.beal@protonmail.ch",
    description="Exquisitor -- EXternal QUestion Internet SITe Online Researcher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dbeal/exquisitor",
    packages=['exquisitor'],
    scripts = [
        'exquisitor/run_session',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
    install_requires=[
        'gom',
    ],
)
