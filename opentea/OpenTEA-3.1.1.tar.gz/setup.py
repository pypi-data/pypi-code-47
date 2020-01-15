#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name="OpenTEA",
    version="3.1.1",
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            "opentea_test_schema = opentea.cli:test_schema",
        ],
    },
    # scripts=[
    #     'bin/opentea'
    # ],

    install_requires=[
        'numpy>=1.16.2',
        'h5py>=2.9.0',
        'jsonschema',
        'Pillow>=5.4.1',
        'PyYAML>=3.13',
        "click",
    ],
    package_data={'opentea': ['gui_forms/images/*.gif']},
    # metadata
    author='Antoine Dauptain, Aimad Er-raiy',
    author_email='coop@cerfacs.fr',
    description='Helpers tools for the setup of Scientific software',
    license="CeCILL-B",
    url='http://cerfacs.fr/coop/',
)
