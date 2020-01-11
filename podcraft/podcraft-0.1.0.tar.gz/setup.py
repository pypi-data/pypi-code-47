# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['podcraft']

package_data = \
{'': ['*']}

install_requires = \
['cached-property>=1.5.1,<2.0.0',
 'click>=7.0,<8.0',
 'podman>=1.6.0,<2.0.0',
 'requests>=2.22.0,<3.0.0',
 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['podcraft = podcraft.cli:main']}

setup_kwargs = {
    'name': 'podcraft',
    'version': '0.1.0',
    'description': 'Minecraft server manager, using podman',
    'long_description': None,
    'author': 'Jamie Bliss',
    'author_email': 'jamie@ivyleav.es',
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
