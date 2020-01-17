#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Wanghaibo
# Mail: dasuda2015@163.com
# Created Time:  2018-4-16 19:17:34
#############################################

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "arxiv_pdf",      #这里是pip项目发布的名称
    version = "0.0.1",  #版本号，数值大的会优先被pip
    keywords = ("pip", "arxiv"),
    description = "download arxiv papers",
    long_description = "download arxiv papers",
    license = "MIT Licence",

    url = "",     #项目相关文件地址，一般是github
    author = "Wanghaibo",
    author_email = "dasuda2015@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["requests","pandas","bs4"]          #这个项目需要的第三方库
)
