# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['r2c_py_ast']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'r2c-py-ast',
    'version': '0.1.0b1',
    'description': 'Program analysis utilities for Python, by r2c. Used in [Bento](https://bento.dev).',
    'long_description': None,
    'author': 'R2C',
    'author_email': 'hello@returntocorp.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://bento.dev',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
