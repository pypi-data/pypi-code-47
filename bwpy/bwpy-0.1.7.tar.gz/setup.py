# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bwpy', 'bwpy.bitwarden']

package_data = \
{'': ['*']}

install_requires = \
['sh>=1.12.14,<2.0.0']

entry_points = \
{'console_scripts': ['bwpy = bwpy.__main__:main']}

setup_kwargs = {
    'name': 'bwpy',
    'version': '0.1.7',
    'description': '',
    'long_description': None,
    'author': 'Rob Wilson',
    'author_email': 'roobert@gmail.com',
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
