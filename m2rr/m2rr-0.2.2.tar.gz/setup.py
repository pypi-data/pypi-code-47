#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme_file = path.join(path.dirname(path.abspath(__file__)), 'README.md')
try:
    from m2rr import parse_from_file
    readme = parse_from_file(readme_file)
except ImportError:
    with open(readme_file) as f:
        readme = f.read()

install_requires = ['mistune', 'docutils']
test_requirements = ['pygments']
if sys.version_info < (3, 3):
    test_requirements.append('mock')

setup(
    name='m2rr',
    version='0.2.2',
    description='Markdown and reStructuredText in a single file.',
    long_description=readme,
    author='Edward Huang',
    author_email='e.huang@gns.cri.nz',
    url='https://github.com/qhua948/m2rr',
    py_modules=['m2rr'],
    entry_points={'console_scripts': 'm2rr = m2rr:main'},
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords='Markdown reStructuredText sphinx-extension',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
    ],
    install_requires=install_requires,
    test_suite='tests',
    tests_require=test_requirements,

)
