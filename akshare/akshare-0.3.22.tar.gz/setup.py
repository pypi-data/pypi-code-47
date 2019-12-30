# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: Albert King
date: 2019/10/16 13:58
contact: jindaxiang@163.com
desc: AkShare 的 pypi 基本信息文件
"""
import re
import ast

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


def get_version_string():
    """
    Get the akshare version number
    :return: str version number
    """
    with open("akshare/__init__.py", "rb") as f:
        version_line = re.search(
            r"__version__\s+=\s+(.*)", f.read().decode("utf-8")
        ).group(1)
        return str(ast.literal_eval(version_line))


setuptools.setup(
    name="akshare",
    version=get_version_string(),
    author="Albert King",
    author_email="jindaxiang@163.com",
    license="MIT",
    description="A tool for downloading financial data!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jindaxiang/akshare",
    packages=setuptools.find_packages(),
    install_requires=[
        "bs4>=0.0.1",
        "lxml>=4.2.1",
        "matplotlib>=3.1.1",
        "numpy>=1.15.4",
        "pandas>=0.25.1",
        "requests>=2.22.0",
        "demjson>=2.2.4",
        "pyexecjs>=1.5.1",
        "pillow>=6.2.0",
        "pypinyin>=0.35.0",
        "websocket-client>=0.56.0",
        "pytrends>=4.7.2",
        "pycryptodomex>=3.9.4",
        "html5lib>=1.0.1",
        "websockets>=8.1",
        # "newspaper3k>=0.2.8",
        "requests-html>=0.10.0",
        "scikit-learn>=0.22",
        "fonttools>=4.2.2",
        "xlrd>=1.2.0",
    ],
    package_data={"": ["*.py", "*.json", "*.pk", "*.woff"]},
    keywords=[
        "stock",
        "option",
        "futures",
        "bond",
        "index",
        "air",
        "others",
        "finance",
        "spider",
        "quant",
        "quantitative",
        "investment",
        "trading",
        "algotrading",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
