# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_lapper']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py-lapper',
    'version': '0.9.0',
    'description': 'A pure python port of nim-lapper.',
    'long_description': None,
    'author': 'Seth Stadick',
    'author_email': 'sstadick@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
