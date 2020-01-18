# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='py-dataflow',
      version='0.0.4',
      description='PySpark application',
      url='http://github.com/junqueira/py-dataflow',
      author='junqueira',
      long_description=read('README.md'),
      author_email='lcjneto@gmail.com',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=[
        'flask_restful',
      ],
      zip_safe=False
)
