"""
@author : Go_Fight_Now(WangSen)
@file   : setup.py
@time   : 2020/01/03 22:18
@docs   : https://docs.python.org/zh-cn/3/
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fight_day",
    version="0.0.2",
    author="Go_Fight_Now",
    author_email="gofightnow.dev@gmail.com",
    description="Daily sentence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
