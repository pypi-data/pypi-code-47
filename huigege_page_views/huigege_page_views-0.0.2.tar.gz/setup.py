#! /usr/bin/env python
# -*- coding: utf-8 -*_
# Author: ***<***gmail.com>
from distutils.core import setup
import setuptools

setup(
    name='huigege_page_views',  # 包的名字
    version='0.0.2',  # 版本号
    description='views_page',  # 描述
    author='Huigege',  # 作者
    author_email='wan5198@qq.com',  # 你的邮箱**
    url='https://github.com/wan5198',  # 可以写github上的地址，或者其他地址
    py_modules=['huigege_page_views.page_views'],  # 包内需要引用的文件夹

    # 依赖包
    install_requires=[

    ],

    zip_safe=True,
)

import huigege_page_views