# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sipy', 'sipy.quantities', 'sipy.units']

package_data = \
{'': ['*']}

install_requires = \
['toml>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'sipy',
    'version': '0.2.1',
    'description': '',
    'long_description': None,
    'author': 'Samuel Broster',
    'author_email': 'sbroster@undo.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
