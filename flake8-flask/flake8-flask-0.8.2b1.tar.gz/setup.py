# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flake8_flask']

package_data = \
{'': ['*']}

install_requires = \
['flake8>=3.7.9,<4.0.0', 'r2c-py-ast==0.1.0b1']

entry_points = \
{'flake8.extension': ['r2c-flake8 = flake8_flask.main:Flake8Flask']}

setup_kwargs = {
    'name': 'flake8-flask',
    'version': '0.8.2b1',
    'description': 'Static analysis checks for Flask, by r2c. Available in our free program analysis tool, Bento. (ht',
    'long_description': None,
    'author': 'grayson',
    'author_email': 'grayson@returntocorp.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
