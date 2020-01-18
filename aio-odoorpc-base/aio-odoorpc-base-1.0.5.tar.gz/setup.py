# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aio_odoorpc_base']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aio-odoorpc-base',
    'version': '1.0.5',
    'description': "Fast, simple Odoo RPC package with sync and async functions to pilot Odoo's jsonrpc API. Check aio-odoorpc for a higher-level, friendlier interface.",
    'long_description': None,
    'author': 'mbello',
    'author_email': 'mbello@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mbello/aio-odoorpc-base',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
