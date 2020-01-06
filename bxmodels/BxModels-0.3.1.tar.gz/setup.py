#
#  setup.py
#  bxmodels
#
#  Created by Oliver Borchert on May 23, 2019.
#  Copyright (c) 2019 Oliver Borchert. All rights reserved.
#

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='BxModels',
    version='0.3.1',

    author='Oliver Borchert',
    author_email='borchero@icloud.com',

    description='Popular Machine Learning Models in PyTorch with Strong GPU Acceleration.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',

    url='https://gitlab.lrz.de/borchero/bxmodels',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    python_requires='>=3.7',
    install_requires=[
        'torch>=1.3.1,<1.4.0',
        'numpy>=1.16.3,<2.0.0',
        'bxtorch>=0.6.0,<0.7.0'
    ],

    license='License :: OSI Approved :: MIT License',
    zip_safe=False
)
