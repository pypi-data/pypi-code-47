# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quantworks', 'quantworks.ext.testcases', 'quantworks.ext.twitter']

package_data = \
{'': ['*']}

install_requires = \
['quantworks==0.21', 'six>=1.13.0,<2.0.0', 'tweepy>=3.8.0,<4.0.0']

setup_kwargs = {
    'name': 'quantworks-twitter',
    'version': '1.0',
    'description': 'Twitter integration for quantworks',
    'long_description': None,
    'author': 'ttymck',
    'author_email': 'tyler@tylerkontra.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
