# -*- coding:utf-8 -*-

from setuptools import setup, find_packages


setup(
    name="py-tratto",
    version="0.0.2",
    packages=find_packages(),
    license="BSD 3-clause",
    install_requires=['pexpect'],
    author="HoxinhLuo",
    author_email="2577229471@qq.com",
    url="https://github.com/HoxinhLuo/pytratto",
    description="Pytratto is a framework built to issue commands to cisco or huawei routers over ssh and telnet which requires pexpect."
)
