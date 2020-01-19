# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['redis_cache']

package_data = \
{'': ['*']}

install_requires = \
['redis>=3.3.11,<4.0.0', 'redis_cache>=0.1.5,<0.2.0']

setup_kwargs = {
    'name': 'redis-simple-cache-py3',
    'version': '0.0.7',
    'description': 'redis-simple-cache is a pythonic interface for creating a cache over redis. It provides simple decorators that can be added to any function to cache its return values.',
    'long_description': None,
    'author': 'Vivek Narayanan, Fl\xc3\xa1vio Juvenal, Sam Zaydel',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
