from setuptools import setup, find_packages

# This call to setup() does all the work
setup(
    name="mp-string-similarity",
    version="2.0.0",
    description="MP string similarity check",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    install_requires=["strsimpy"],
)
