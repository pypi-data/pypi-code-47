# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tellor']

package_data = \
{'': ['*'], 'tellor': ['abi/*']}

install_requires = \
['web3>=5.4.0,<6.0.0']

setup_kwargs = {
    'name': 'tellor',
    'version': '0.3.8',
    'description': 'python wrapper for tellor decentralized oracle',
    'long_description': None,
    'author': 'banteg',
    'author_email': 'banteeg@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
