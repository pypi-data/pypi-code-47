
from setuptools import setup, find_packages

setup(
    name='domcmc',
    version='1.0.0',
    url='https://gitlab.science.gc.ca/dja001/domcmc',
    license='GPL-3.0-or-later',
    author='Dominik Jacques',
    author_email='dominik.jacques@gmail.com',
    description="dominik's tools for reading fst files",
    long_description='README.md',
    long_description_content_type="text/markdown",
    packages=find_packages(),    
    install_requires=['python >= 3.7.0', 'numpy >= 1.17.0' ],
)
