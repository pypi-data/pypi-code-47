#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: LiangjunFeng
# Mail: zhumavip@163.com
# Created Time:  2018-4-16 19:17:34
#############################################

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "ym-xadmin",      #这里是pip项目发布的名称
    version = "0.0.5",  #版本号，数值大的会优先被pip
    keywords = ("pip", "python3","xadmin"),
    description = "xadmin for python3",
    long_description = "An feature extraction algorithm, improve the FastICA",
    license = "MIT Licence",

    url = "https://github.com/LiangjunFeng/SICA",     #项目相关文件地址，一般是github
    author = "",
    author_email = "",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
 
)
