# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 20:33:28 2020

@author: user
"""
import setuptools
 
with open("README.txt", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    #Here is the module name.
    name="mytopsis",
 
    #version of the module
    version="0.0.1",
 
    #Name of Author
    author="Sapna Goyal",
 
    #your Email address
    author_email="sp2000jeea@gmail.com",
 
    #Small Description about module
    description="finding ranks and scores row wise of a dataset according to given weights of columns and impacts that they will have on output.",
 
    long_description=long_description,
 
    #Specifying that we are using markdown file for description
    long_description_content_type="text/plain",
 
    #Any link to reach this module, if you have any webpage or github profile
    #url="https://github.com/Pushkar-Singh-14/",
    packages=setuptools.find_packages(),
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)