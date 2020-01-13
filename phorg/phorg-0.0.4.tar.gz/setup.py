# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['phorg']
entry_points = \
{'console_scripts': ['phorg = phorg:main']}

setup_kwargs = {
    'name': 'phorg',
    'version': '0.0.4',
    'description': "Command-line application to help reduce photography's organization time consumption.",
    'long_description': None,
    'author': 'NunoPalma',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/NunoPalma/Photography-Organizer',
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '==3.0.0',
}


setup(**setup_kwargs)
