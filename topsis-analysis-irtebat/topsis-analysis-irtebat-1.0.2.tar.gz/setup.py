from setuptools import *

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="topsis-analysis-irtebat",
    version="1.0.2",
    description="Topsis analysis of a csv file",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/irtebat/topsis-analysis",
    author="Irtebat",
    author_email="irtebat.10@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["TOPSIS_package"],
    include_package_data=True,
    install_requires=["numpy","pandas"],
    entry_points={
        "console_scripts": [
            "topsis=TOPSIS_package.cli:main",
        ]
    },
)