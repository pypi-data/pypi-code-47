# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['swarm_regulator', 'swarm_regulator.event_types']

package_data = \
{'': ['*'], 'swarm_regulator': ['fixtures/*']}

install_requires = \
['aiodocker>=0.17.0,<0.18.0', 'pytest-asyncio>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'swarm-regulator',
    'version': '0.1.0',
    'description': 'The regulator of your Docker Swarm cluster',
    'long_description': None,
    'author': 'Paris Kasidiaris',
    'author_email': 'paris@sourcelair.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
