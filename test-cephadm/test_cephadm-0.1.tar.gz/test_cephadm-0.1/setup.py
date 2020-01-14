import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='test_cephadm',  
     version='0.1',
     scripts=['cephadm'] ,
     author="ceph",
     author_email="ceph@ceph.com",
     description="cephadm",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/ceph/ceph",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
