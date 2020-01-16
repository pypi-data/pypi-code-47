#!/usr/bin/env python3

from setuptools import find_packages, setup

INSTALL_REQUIRES = ['numpy', 'scikit-learn', 'scipy']
TESTS_REQUIRE = []

setup(
    name='franklab_msdrift',
    version='0.1.9.dev0',
    license='',
    description=(''),
    author='',
    author_email='',
    url='',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    include_package_data=True,
)
