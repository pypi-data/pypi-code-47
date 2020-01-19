# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cmdlib']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cmdlib',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Xavier Martinez-Hidalgo',
    'author_email': 'xavier@martinezhidalgo.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
