# -*- coding: utf-8 -*-
from __future__ import with_statement

import sys

from setuptools import setup, find_namespace_packages


# Do not change the variable name.  It's parsed by doc/conf.py script.
version = '0.1.6a1.post2'

requires = ['Sphinx >= 1.2', 'six']

if 'bdist_wheel' not in sys.argv and sys.version_info < (2, 7):
    requires.append('argparse')


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='Paebbels.sphinxcontrib.autoprogram',
    version=version,
    url='https://github.com/Paebbels/Paebbels.sphinxcontrib.autoprogram',
    license='2-Clause BSD',
    author='Hong Minhee, Patrick Lehmann',
    author_email='\x68\x6f\x6e\x67.minhee' '@' '\x67\x6d\x61\x69\x6c.com, Paebbels@gmail.com',
    description='Documenting CLI programs',
    long_description=readme(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Topic :: Utilities'
    ],
    platforms='any',
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=requires,
    extras_requires={":python_version=='2.6'": ['argparse']},
    test_suite='Paebbels.sphinxcontrib.autoprogram.suite'
)
