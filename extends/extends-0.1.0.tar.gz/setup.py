# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['extends']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'extends',
    'version': '0.1.0',
    'description': 'A simple Python library that adds a decorator which helps extend functionality classes by new methods without inheritanting them',
    'long_description': None,
    'author': 'Arthur Hakimov',
    'author_email': 'verybigfolder@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
