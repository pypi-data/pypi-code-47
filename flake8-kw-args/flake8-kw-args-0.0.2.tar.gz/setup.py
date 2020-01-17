"""
Setup the package.
"""
from setuptools import (
    find_packages,
    setup,
)

DESCRIPTION = 'Flake8 plugin to check explicitly passed arguments.'
URL = 'https://github.com/casafari/flake8-kw-args'

with open('README.md', 'r') as read_me:
    long_description = read_me.read()

with open('requirements/project.txt', 'r') as requirements_file:
    requirements = requirements_file.read().splitlines()

with open('.project-version', 'r') as project_version_file:
    project_version = project_version_file.read().strip()


setup(
    version=project_version,
    name='flake8-kw-args',
    author='Casafari',
    author_email='tools@casafari.net',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=URL,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'flake8.extension': [
            'KWA = flake8_kw_args:Plugin',
        ]
    },
)
