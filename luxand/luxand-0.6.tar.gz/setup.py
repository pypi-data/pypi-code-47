#!/usr/bin/env python3
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='luxand',  
     version='0.6',
     scripts=['luxand.py'] ,
     author="Alexander Boykov",
     author_email="alex@luxand.cloud",
     description="Luxand.Cloud API",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/realairgrow/luxand.git",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
