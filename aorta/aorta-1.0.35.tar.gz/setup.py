#!/usr/bin/env python3
from setuptools import find_packages
from setuptools import setup


setup(
    name='aorta',
    version='1.0.35',
    description='AMQP Durable Messaging Library',
    author='Cochise Ruhulessin',
    author_email='c.ruhulessin@ibrb.org',
    url='https://www.ibrb.org',
    install_requires=[
        'pytz',
        'python-qpid-proton==0.28.0',
	    'PyYAML>=5.1.2',
        'marshmallow>=3.0.1',
        'python-ioc>=1.3.11',
        'dsnparse>=0.1.15',
    ],
    packages=find_packages(),
    license="GPLv3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Clustering",
        "Topic :: System :: Distributed Computing"
    ]
)
