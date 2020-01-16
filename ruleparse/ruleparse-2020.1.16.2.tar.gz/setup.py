# -*- coding: utf-8 -*-
"""
    Setup file for ruleparse.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 3.2.3.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
# import sys
#
# from pkg_resources import VersionConflict, require
from setuptools import find_packages, setup
#
# try:
#     require('setuptools>=38.3')
# except VersionConflict:
#     print("Error: version of setuptools is too old (<38.3)!")
#     sys.exit(1)

VERSION = "2020.1.16.2"

def install_requires():
    install_requires = []
    with open("requirements.txt", "r") as f:
        for line in f:
            install_requires.append(line.strip())
    return install_requires

if __name__ == "__main__":

    setup(
        name='ruleparse',
        version=VERSION,
        description='规则解析框架',
        url="",
        long_description="定义规则解析的基类与规则解析项目的基本结构，并提供生成规则解析项目模板脚本",
        author='niyoufa',
        author_email='niyoufa@aegis-data.cn',
        packages=find_packages(),
        scripts=[],
        install_requires=install_requires(),
    )
