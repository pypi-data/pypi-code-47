#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    'elasticsearch>=7.0.0,<8.0.0',
    'boto3>=1.10.49',
    'python-configuration>=0.5.0',
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Emanuel Gardaya Calso",
    author_email='pypi@bloodpet.com',
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
    description="Restore selected logs from S3 to Elasticsearch",
    entry_points={
        'console_scripts': [
            'partial_s3_to_es=partial_s3_to_es.cli:main',
            's3_to_es=partial_s3_to_es.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='partial_s3_to_es',
    name='partial_s3_to_es',
    packages=find_packages(include=['partial_s3_to_es', 'partial_s3_to_es.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bloodpet/partial_s3_to_es',
    version='0.1.0',
    zip_safe=False,
)
