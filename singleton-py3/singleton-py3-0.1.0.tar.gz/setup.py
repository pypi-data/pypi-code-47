# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['singleton']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'singleton-py3',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'David Jim\xc3\xa9nez',
    'author_email': 'davigetto@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
