# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netizenship']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['netizenship = netizenship:main']}

setup_kwargs = {
    'name': 'netizenship',
    'version': '0.1.1',
    'description': 'A Tool to check the online membership in popular websites like Facebook, Twitter, etc.',
    'long_description': None,
    'author': 'Rahul Raj',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.8',
}


setup(**setup_kwargs)
