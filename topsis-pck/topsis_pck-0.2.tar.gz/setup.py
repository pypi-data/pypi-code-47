import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='topsis_pck',  
     version='0.2',
     scripts=['topsis'] ,
     author="Ritik",
     author_email="ritikgupta3008@gmail.com",
     description="topsis package in python",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/rg3456/topsis_pck",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )