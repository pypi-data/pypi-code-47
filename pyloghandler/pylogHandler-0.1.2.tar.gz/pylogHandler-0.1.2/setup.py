#############################################
# File Name: setup.py
# Author: renoyuan
# Mail: renoyuan@foxmail.com
# Created Time:  2019-12-30 19:17:34
#############################################


from setuptools import setup, find_packages

setup(
    name="pylogHandler",
    version="0.1.2",
    # keywords=("pip", "pathtool", "timetool", "magetool", "mage"),
    description="renoyuan log",
    long_description="renoyuan log",
    license="MIT Licence",

    url="https://github.com/yhyPython110/pylogHandler.git",
    author="renoyuan",
    author_email="renoyuan@foxmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    # install_requires=[]
)
