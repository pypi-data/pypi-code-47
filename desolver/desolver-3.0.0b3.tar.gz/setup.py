#!/usr/bin/env python
"""
The MIT License (MIT)

Copyright (c) 2019 Microno95, Ekin Ozturk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import absolute_import, division, print_function, unicode_literals

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='desolver',
      version='3.0.0b3',
      description='Differential Equation System Solver',
      author='Ekin Ozturk',
      author_email='ekin.ozturk@mail.utoronto.ca',
      long_description=long_description,
      long_description_content_type="text/markdown",
      install_requires=['numpy', 'tqdm', 'scipy>=0.18.0'],
      license='MIT',
      keywords=['ode solver', 'differential equation', 'differential system', 'ode system', 'non-linear ode'],
      url='https://github.com/Microno95/desolver',
      packages=['desolver', 'desolver.integration_schemes', 'desolver.exception_types', 'desolver.utilities', 'desolver.backend'],
      extras_require={
        'pyaudi':   ["pyaudi>=1.7"],
        'pytorch':  ["torch>=1.3.1", "torchvision>=0.4.2"],
      },
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 4 - Beta',

          'Environment :: Console',
          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Intended Audience :: Education',
          'Intended Audience :: End Users/Desktop',
          'Topic :: Scientific/Engineering :: Mathematics',

          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: MIT License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7'
      ],
      )
