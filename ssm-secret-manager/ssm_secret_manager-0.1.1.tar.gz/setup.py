import setuptools
from os import path


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='ssm_secret_manager',
    version='0.1.1',
    url='https://github.com/bklim5/aws-ssm-secret-manager',
    description='SecretManager class to retrieve secrets from AWS System Manager Parameter Store',
    author='BK Lim',
    author_email='bklim5@hotmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'boto3'
    ],
    keywords = ['secret manager', 'AWS', 'Parameter Store'], 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)