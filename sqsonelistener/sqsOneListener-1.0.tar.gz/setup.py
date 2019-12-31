from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


setup(
    name='sqsOneListener',
    version='1.0',
    description='A simple Python SQS utility package',

    # The project's main homepage.
    # url='https://github.com/jegesh/python-sqs-listener',

    # Author details
    author='Benlolo Noam',

    # Choose your license
    license='Apache Software License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='aws sqsOneListener listener',
    packages=find_packages(),
    install_requires=['boto3']
)