import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='generateGUID',
     version='1.4',
     author="jeremy garcia",
     author_email="jeremy.garcia@univ-amu.fr",
     description="",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/Slowblitz/GUID-core",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
