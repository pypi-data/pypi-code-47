"""
dynamite
========

Use dynamite to keep a postgres replica of one or more dynamodb
tables. At its core, dynamite is an AWS Lambda event handler for
processing dynamodb streams record events and shuttling those record
events into an associated postgres database. Dynamite only has a
couple of pure python dependencies all of which make it easy to make
dynamite into sand-alone Lambda Function.
"""
import re
import ast
from setuptools import setup

_version_re = re.compile(r'__version__\s*=\s*(.*)\s*')

setup(
    name='dynamite-streams',
    version='0.0.1',
    url='http://github.com/dbish/dynamite',
    license='Apache License Version 2',
    author='Dillon Hicks',
    author_email='chronodynamic@gmail.com',
    description='A module to be used as an AWS Lambda function to keep postgres replicas of dynamodb tables.',
    long_description=__doc__,
    packages=['dynamite'],
    package_data={},
    include_package_data=True,
    platforms='any',
    install_requires=["boto3", "sqlalchemy", "pg8000"],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: System :: Archiving :: Mirroring'
    ],
    python_requires ='>=3.7',
)
