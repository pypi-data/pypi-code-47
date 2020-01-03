# from distutils.core import setup
from setuptools import setup
import os


rootdir = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(rootdir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="py_str_case",
    version="0.0.3",
    author="shiva",
    author_email="shivashanker.chagamreddy@gmail.com",
    description="String case converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShivaShankerReddy/py_string_case",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # scripts= ['pystrcase/py_str_case.py'],
    py_modules=[
        'py_str_case'
    ],
    python_requires='>=3.0',
)
