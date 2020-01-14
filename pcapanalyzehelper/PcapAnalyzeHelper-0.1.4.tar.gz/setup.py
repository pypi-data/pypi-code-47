from setuptools import setup

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="PcapAnalyzeHelper",
    version="0.1.4",
    author="wenjwang",
    author_email="wenjade91@gmail.com",
    packages=["PcapAnalyzeHelper"],
    install_requires=["numpy", "pandas", "scapy", "matplotlib", "seaborn"],
    zip_safe=False,
    license="MIT",
    description="A python package for quick analysis on pcap file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
)

