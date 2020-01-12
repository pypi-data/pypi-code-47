from setuptools import setup, Extension, find_packages
from distutils.core import setup


from codecs import open
import os
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'edgell-README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
      # Information
      name = "edgell",
      version = "1.1",
      description='ipyparallel wrapper for data scientists',
      url = "https://github.com/freedomtowin/edgell",
      author = "Rohan Kotwani",
      
      
      license = "MIT",
      classifiers=[
                   "Development Status :: 4 - Beta",
                   # Indicate who your project is intended for
                   "Intended Audience :: Developers",
                   "Intended Audience :: Science/Research",
                   "Topic :: Software Development",
                   "Topic :: Scientific/Engineering",
                   
                   # Pick your license as you wish
                   'License :: OSI Approved :: MIT License',
                   
                   # Specify the Python versions you support here. In particular, ensure
                   # that you indicate whether you support Python 2, Python 3 or both.
                   'Programming Language :: Python :: 3'
                   ],
      keywords = "ipyparallel parallel edgell analytics sklearn xgboost",
      #    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
  packages=['edgell'],  # Required
      install_requires = ["numpy","ipyparallel"],
      python_requires = ">=3.6",
      ext_modules = [Extension("edgell.edge_parallel",
                               ['edgell/edge_parallel.py'],
                               include_dirs=[])]
      
      )
