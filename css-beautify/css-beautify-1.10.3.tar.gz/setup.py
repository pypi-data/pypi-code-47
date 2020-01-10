#!/usr/bin/env python

from setuptools import setup
from cssbeautifier.__version__ import __version__

setup(name='css-beautify',
        version=__version__,
        description='CSS unobfuscator and beautifier',
        author='Jorengarenar',
        author_email='jorengarenar@protonmail.com',
        entry_points={
            'console_scripts': [
                'css-beautify = cssbeautifier:main'
                ]
            },
        packages=['cssbeautifier'],
        license='MIT',
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ],
        python_requires='>=3.6',
        )
