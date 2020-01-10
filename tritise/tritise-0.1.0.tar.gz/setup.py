# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tritise']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'sqlalchemy>=1.3.12,<2.0.0']

entry_points = \
{'console_scripts': ['tritise = tritise.cli:cli']}

setup_kwargs = {
    'name': 'tritise',
    'version': '0.1.0',
    'description': 'A small python library to handle trivial time series in an SQLite database.',
    'long_description': None,
    'author': 'asmw',
    'author_email': 'asmw@asmw.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
