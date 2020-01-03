"""
.. module:: setup
   :synopsis: Installation information for pact_state_provider
"""
# Standard
import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

INSTALL_REQUIRES = ['setuptools', 'click']


setup(
    name='pact_state_provider',
    version='1.0.7',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    license='Apache-2.0',
    description='Simple server to provide an endpoint used by pact to generate a provider state',
    long_description=README,
    long_description_content_type='text/x-rst',
    url='https://github.com/nalch/pact-state-provider',
    author='nalch',
    author_email='Scholze.Kristian@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=INSTALL_REQUIRES,
    entry_points={
        'console_scripts': [
            'pact-state-provider = pact_state_provider:pact_state_provider',
        ],
    },
)
