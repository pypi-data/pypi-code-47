from setuptools import *

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="topsis-neeraj",
    version="0.0.1",
    description="Topsis Analysis",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/topsis-neeraj",
    author="Neeraj Kapoor",
    author_email="nkapoor50_be18@thapar.edu",
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
