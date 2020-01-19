import os
from setuptools import setup, find_packages


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


setup(
    name='pyjstage',
    version='0.0.1',
    description='J-STAGE API wrapper for Python',
    author='matsurih',
    author_email='pipikapu@gmail.com',
    url='https://github.com/matsurih/pyjstage',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=read_requirements(),
)
