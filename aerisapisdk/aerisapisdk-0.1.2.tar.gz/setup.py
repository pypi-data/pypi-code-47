# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aerisapisdk']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'pathlib>=1.0.1,<2.0.0', 'requests>=2.22,<3.0']

entry_points = \
{'console_scripts': ['aeriscli = aerisapisdk.cli:main']}

setup_kwargs = {
    'name': 'aerisapisdk',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
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
