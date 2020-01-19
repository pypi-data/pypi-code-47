# from distutils.core import setup
from setuptools import setup


def read_file():
      with open("README.rst", encoding="utf-8") as rf:
            return rf.read()


setup(name="wcltestlib", version="1.0.1", description="this is a testlib", packages=["testlib"],
      py_modules=["Tool"], author="wcl", author_email="wcl0729@163.com", long_description=read_file(),
      url="https://github.com/wcl1997/PythonCode", license="MIT")