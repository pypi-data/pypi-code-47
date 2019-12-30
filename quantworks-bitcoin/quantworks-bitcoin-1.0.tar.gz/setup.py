# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quantworks',
 'quantworks.ext.bitcoincharts',
 'quantworks.ext.bitstamp',
 'quantworks.ext.testcases']

package_data = \
{'': ['*']}

install_requires = \
['quantworks==0.21', 'requests>=2.22.0,<3.0.0', 'six>=1.13.0,<2.0.0']

setup_kwargs = {
    'name': 'quantworks-bitcoin',
    'version': '1.0',
    'description': 'Bitcoin integrations for quantworks',
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
