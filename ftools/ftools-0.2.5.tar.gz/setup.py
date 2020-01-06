# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ftools']

package_data = \
{'': ['*']}

install_requires = \
['cardinality>=0.1.1,<0.2.0', 'mypy_extensions>=0.4.3,<0.5.0']

setup_kwargs = {
    'name': 'ftools',
    'version': '0.2.5',
    'description': 'Functional programming utilities',
    'long_description': None,
    'author': 'Iddan Aaronsohn',
    'author_email': 'mail@aniddan.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
