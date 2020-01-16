# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mebula']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=1.7.11,<2.0.0', 'oci>=2.9.0,<3.0.0']

setup_kwargs = {
    'name': 'mebula',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Matt Williams',
    'author_email': 'matt@milliams.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
