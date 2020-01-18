# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['throttlestop']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.16,<2.0', 'plumbum>=1.6,<2.0']

entry_points = \
{'console_scripts': ['throttlestop = throttlestop.__main__:main',
                     'throttlestop-install-service = '
                     'throttlestop.install:main']}

setup_kwargs = {
    'name': 'throttlestop',
    'version': '0.0.5',
    'description': 'Simple tool to manage throttling problems on Linux',
    'long_description': None,
    'author': 'Angus Hollands',
    'author_email': 'goosey15@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
