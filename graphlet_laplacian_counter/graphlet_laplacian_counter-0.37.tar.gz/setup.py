#!/usr/bin/env python

from distutils.core import setup, Extension

setup(name='graphlet_laplacian_counter',
      version='0.37',
      description='Wrapper C++ Graphlet Laplacian Counter',
      author='Sam F. L. Windels',
      author_email='sam.windels@gmail.com',
      # url='https://www.python.org/sigs/distutils-sig/',
      requires=['numpy'], #external packages as dependencies
      packages=['graphlet_laplacian_counter'],
      # package_dir={'': 'src'},
      package_dir={'graphlet_laplacian_counter': 'src/graphlet_laplacian_counter'},
      package_data={'graphlet_laplacian_counter': ['src_c++/*.cpp', 'src_c++/*.h']},
      # ext_modules = [Extension("_counter",['graphlet_laplacian_counter/c++_src/Counter.cpp'], include_dirs=['src_c++'])]
     )
