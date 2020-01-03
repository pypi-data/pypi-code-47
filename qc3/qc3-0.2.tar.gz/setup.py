#!/usr/bin/env python

"""Setup script for qc."""

try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup


setup(
  name = 'qc3',
  version = '0.2',
  description = 'QuickCheck: randomized testing made trivial. Forked to make it work with Python 3.',
  author = 'Peter Scott, Pawel Troka',
  author_email = 'peter@greplin.com, pawel.troka@outlook.com',
  url = 'https://github.com/PawelTroka/qc3',
  package_dir = {'':'src'},
  packages = ['qc'],
  zip_safe = True,
  test_suite = 'nose.collector',
  include_package_data = True,
  license = 'Apache',
  classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Testing',
      'License :: OSI Approved :: Apache Software License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.2',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
  ],
  keywords='qc'
)
