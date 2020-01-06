# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['variable_updater']

package_data = \
{'': ['*']}

install_requires = \
['hvac>=0.9.6,<0.10.0', 'pyyaml>=5.2,<6.0', 'requests>=2.22.0,<3.0.0']

entry_points = \
{'console_scripts': ['variable-updater = variable_updater.__main__:main']}

setup_kwargs = {
    'name': 'variable-updater',
    'version': '0.0.9',
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
