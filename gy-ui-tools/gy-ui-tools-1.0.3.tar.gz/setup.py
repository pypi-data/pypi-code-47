#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/14'

from distutils.core import setup

setup(
    name="gy-ui-tools",  # 这里是pip项目发布的名称
    version="1.0.3",  # 版本号，数值大的会优先被pip
    keywords=["init", "auto-test","ui"],
    description="to simplify auto test",
    long_description="A init package,to simplify develope auto test",
    license="MIT Licence",

    url="https://github.com/xuepl/gy-ui-tool",  # 项目相关文件地址，一般是github
    author="xuepl",
    author_email="xuepl@guoyasoft.com",
    packages=['tool'],
    platforms="python",
    install_requires=[
        'pinyin==0.4.0',
        'PyMySQL==0.9.3',
        'PyYAML==5.1.2',
        'allure-pytest==2.7.0',
        'pytest==5.0.1',
        'zipp==0.6.0',
        'xlwt==1.3.0',
        'xlrd==1.2.0',
        'selenium==3.141.0',
        'pyautoit-win64==1.0.3'


    ]
)
