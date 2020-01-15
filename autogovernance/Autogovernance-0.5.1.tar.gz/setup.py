# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 09:36:01 2020

@author: LP885RH
"""

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='Autogovernance',
      version='0.5.1',
      description='Package to update information in Governance',
      url='https://github.com/JulioPestanaSalinas/AutoGovernance',
      author='Julio Pestaña Salinas',
      author_email='Julio.Pestana.Salinas@es.ey.com',
      license='GNU',
      packages=['autogovernance'],
      zip_safe=False,
      python_requires='>=3.6',
      long_description=long_description,
      long_description_content_type='text/markdown'
      )