# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['clifier']

package_data = \
{'': ['*'], 'clifier': ['examples/*']}

install_requires = \
['PyYAML>=5.3,<6.0']

setup_kwargs = {
    'name': 'clifier',
    'version': '0.0.3',
    'description': 'Clifier is a simple, tiny script to generate Argparse commands and subparsersfrom yaml config file.',
    'long_description': None,
    'author': 'xnuinside',
    'author_email': 'xnuinside@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
