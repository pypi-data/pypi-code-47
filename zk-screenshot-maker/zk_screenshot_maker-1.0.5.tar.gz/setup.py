#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: JeffreyCao
# Mail: jeffreycao1024@gmail.com
# Created Time:  2019-11-16 21:48:34
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#package-data
#############################################

# from setuptools import setup, find_packages  # 这个包没有的可以pip一下
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zk_screenshot_maker",
    version="1.0.5",
    keywords=("pip", "zk_screenshot_maker"),
    description="Tool to make screenshots for apple app store",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT Licence",

    url="https://github.com/caojianfeng/zk_logo_maker",
    author="JeffreyCao",
    author_email="jeffreycao1024@gmail.com",

    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        'zk_screenshot_maker': [
            'theme/ZhenyanGB.ttf',
            'theme/SourceHanSansCN-Normal.ttf',
            'theme/bg_0_2048x2732.png',
            'theme/bg_1_2048x2732.png',
            'theme/bg_2_2048x2732.png',
            'theme/bg_3_2048x2732.png',
            'theme/bg_4_2048x2732.png',
            'theme/bg_5_2048x2732.png',
            'theme/bottom_frame_2048x606.png'
        ],
    },
    platforms="any",
    install_requires=["Pillow"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'zk-screenshot-maker = zk_screenshot_maker.__main__:main'
        ]
    }
)
