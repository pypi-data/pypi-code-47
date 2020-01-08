# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trase']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'trase',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Trase Team',
    'author_email': 'info@trase.earth',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
