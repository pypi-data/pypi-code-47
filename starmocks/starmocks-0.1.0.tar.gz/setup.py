# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['starmocks']
install_requires = \
['attrdict>=2.0,<3.0']

setup_kwargs = {
    'name': 'starmocks',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Pedro Werneck',
    'author_email': 'pjwerneck@gmail.com',
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
