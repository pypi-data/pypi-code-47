from setuptools import setup
from fool_house import __version__

with open("README.md") as f:
    long_description = f.read()

setup(
    name="Fool-house",
    description="Yellow house",
    long_description=long_description,
    keywords=["YELLOW", "FOOL", "HOUSE", "CORPSMAN", "SCHIZO", "COUNT"],
    author="Andreew Gregory",
    author_email='6squaress@gmail.com',
    url="https://github.com/1Gregory/fool-house",
    download_url="https://github.com/1Gregory/fool-house/archive/1.0.tar.gz",
    version=__version__,
    install_requires=[],
    packages=["fool_house"],
    license="MIT",
)
