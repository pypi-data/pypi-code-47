# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['consuela']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'consuela',
    'version': '0.1.0',
    'description': 'Format and linters pack',
    'long_description': None,
    'author': 'Nick Sablukov',
    'author_email': 'dessanndes@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
