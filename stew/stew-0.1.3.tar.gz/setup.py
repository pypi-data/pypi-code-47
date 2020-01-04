# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stew']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'stew',
    'version': '0.1.3',
    'description': 'A library for parsing localization string files',
    'long_description': None,
    'author': 'Timofey Danshin',
    'author_email': 't.danshin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
