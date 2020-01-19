# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['adonai_client']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.11.1,<0.12.0', 'sgqlc>=9.1,<10.0']

setup_kwargs = {
    'name': 'adonai-client',
    'version': '0.1.8',
    'description': 'Client for adonai server',
    'long_description': None,
    'author': 'Aleksander Lavrov',
    'author_email': 'egnod@ya.ru',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
