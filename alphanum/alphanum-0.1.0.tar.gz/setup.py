# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alphanum']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'alphanum',
    'version': '0.1.0',
    'description': 'Generates random alphanumeric strings.',
    'long_description': None,
    'author': 'Cody Logan',
    'author_email': 'clpo13@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
