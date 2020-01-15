import os
import re
import sys
import codecs
from os import path
from io import open
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')


setup(
    name='email_reader',  
    version= find_version("src/email_reader", "__init__.py"),

    description='Sample email reader ',  
    long_description=readme + '\n\n' + history,
    author='Chelladurai',
    author_email='acdurai04@gmail.com',
    url='https://github.com/acdurai/email_reader',
    package_dir={'': 'src'},
    packages=find_packages(where='src',exclude=['docs', 'tests']),
    
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    install_requires=['cryptography'],
    include_package_data=True,

   

    

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/acdurai/email_reader/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/acdurai/email_reader/',
    },
)
