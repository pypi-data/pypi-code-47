#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'requests>=2.22.0']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Aidan Melen",
    author_email='aidan-melen@pluralsight.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Make it easier to interact with the confluent kafka connect REST api.",
    entry_points={
        'console_scripts': [
            'kc=confluent_kafka_connect_cli.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='confluent_kafka_connect_cli',
    name='confluent_kafka_connect_cli',
    packages=find_packages(include=['confluent_kafka_connect_cli']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/aidan-melen/confluent_kafka_connect_cli',
    version='0.3.0',
    zip_safe=False,
)
