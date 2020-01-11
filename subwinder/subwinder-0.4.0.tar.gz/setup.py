# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['subwinder']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'subwinder',
    'version': '0.4.0',
    'description': '',
    'long_description': None,
    'author': 'Lovecraftian Horror',
    'author_email': 'LovecraftianHorror@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
