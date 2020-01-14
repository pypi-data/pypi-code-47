# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['obstacle']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=19.3.0,<20.0.0',
 'click>=7.0,<8.0',
 'dill>=0.3.1,<0.4.0',
 'gym>=0.15.4,<0.16.0',
 'mlagents-envs==0.10',
 'opencv-contrib-python>=4.1.2,<5.0.0',
 'opencv-python>=4.1.2,<5.0.0',
 'pendulum>=2.0.5,<3.0.0',
 'pyyaml>=5.2,<6.0',
 'toml>=0.10.0,<0.11.0',
 'torch>=1.3.1,<2.0.0',
 'wget>=3.2,<4.0']

entry_points = \
{'console_scripts': ['ariadne = obstacle.console:cli']}

setup_kwargs = {
    'name': 'obstacle',
    'version': '0.1.0',
    'description': 'Obstacle Tower Challenge Environment',
    'long_description': None,
    'author': 'Stelios Tymvios',
    'author_email': 'solliet@protonmail.com',
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
