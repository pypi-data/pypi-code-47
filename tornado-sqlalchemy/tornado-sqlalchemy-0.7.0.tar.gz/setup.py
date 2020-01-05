# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tornado_sqlalchemy']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.3,<2.0', 'tornado>=6.0,<7.0']

setup_kwargs = {
    'name': 'tornado-sqlalchemy',
    'version': '0.7.0',
    'description': 'SQLAlchemy support for Tornado',
    'long_description': None,
    'author': 'Siddhant Goel',
    'author_email': 'me@sgoel.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/siddhantgoel/tornado-sqlalchemy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
