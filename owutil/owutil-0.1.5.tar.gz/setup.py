# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['owutil']
entry_points = \
{'console_scripts': ['owutil = owutil:main']}

setup_kwargs = {
    'name': 'owutil',
    'version': '0.1.5',
    'description': '',
    'long_description': None,
    'author': 'drys262',
    'author_email': 'koeichavez17@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
