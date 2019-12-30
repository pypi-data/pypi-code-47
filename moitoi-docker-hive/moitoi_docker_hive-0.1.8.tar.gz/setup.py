#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 'docker',
                 'paramiko',
                 'flask',
                 'flask_restful',
                 'pyyaml'
               ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Andres Kepler",
    author_email='andres@kepler.ee',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="MoiToi Docker Hive is simple dockrized containers manager",
    entry_points={
        'console_scripts': [
            'mdh=moitoi_docker_hive.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='moitoi_docker_hive',
    name='moitoi_docker_hive',
    packages=find_packages(include=['moitoi_docker_hive', 'moitoi_docker_hive.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/kepsic/moitoi_docker_hive',
    version='0.1.8',
    zip_safe=False,
)
