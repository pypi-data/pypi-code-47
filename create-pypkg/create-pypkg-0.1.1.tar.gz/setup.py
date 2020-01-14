#!/usr/bin/env python

from setuptools import find_packages, setup

from createpypkg import __version__

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='create-pypkg',
    version=__version__,
    author='Daichi Narushima',
    author_email='dnarsil+github@gmail.com',
    description='Python package scaffold builder',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dceoy/create-pypkg',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['docopt', 'jinja2'],
    entry_points={
        'console_scripts': ['create-pypkg=createpypkg.cli.main:main']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development'
    ],
    python_requires='>=3.6'
)
