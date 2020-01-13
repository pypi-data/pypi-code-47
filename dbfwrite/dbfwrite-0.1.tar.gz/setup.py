import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='dbfwrite',  
     version='0.1',
     author="Wenyu Li",
     author_email="vanelwy@gmail.com",
     description="A package for converting dataframe to DBF file",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/vanelwy",
     python_requires=">=3.0",
     packages = ["dbfwrite"],
     install_requires=[
        'datetime',
        'pandas',
        ],
     classifiers=[
         "Programming Language :: Python :: 3.7",
         "License :: OSI Approved :: MIT License",
         "Operating System :: Microsoft",
     ],
     zip_safe=True,
 )

