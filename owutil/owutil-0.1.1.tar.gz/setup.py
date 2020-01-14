# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['owutil']
entry_points = \
{'console_scripts': ['owutil = owutil:main']}

setup_kwargs = {
    'name': 'owutil',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'drys262',
    'author_email': 'koeichavez17@gmail.com',
    'url': None,
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
