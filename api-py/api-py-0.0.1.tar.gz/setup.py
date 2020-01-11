# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['voxel51', 'voxel51.apps', 'voxel51.cli', 'voxel51.users']

package_data = \
{'': ['*']}

install_requires = \
['argcomplete>=1.11.0,<2.0.0',
 'future>=0.18.2,<0.19.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'requests-toolbelt>=0.9.1,<0.10.0',
 'requests>=2.22.0,<3.0.0',
 'six>=1.13.0,<2.0.0',
 'tabulate>=0.8.6,<0.9.0',
 'tzlocal>=2.0.0,<3.0.0']

setup_kwargs = {
    'name': 'api-py',
    'version': '0.0.1',
    'description': 'Python client library for the Voxel51 Platform API.',
    'long_description': None,
    'author': 'Voxel51, Inc.',
    'author_email': 'support@voxel51.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
