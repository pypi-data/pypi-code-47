# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['slideshow']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'slideshow',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'arjoonn sharma',
    'author_email': 'arjoonn.94@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
