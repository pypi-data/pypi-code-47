# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['netizenship']
entry_points = \
{'console_scripts': ['netizenship = netizenship:main']}

setup_kwargs = {
    'name': 'netizenship',
    'version': '0.1.2',
    'description': 'Tool to check the username with popular websites for membership',
    'long_description': None,
    'author': 'Rahul Raj',
    'author_email': 'rahulrajpl@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
