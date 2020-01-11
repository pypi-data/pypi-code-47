# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['edgar3']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=0.25.3,<0.26.0', 'requests>=2.22.0,<3.0.0']

setup_kwargs = {
    'name': 'edgar3',
    'version': '1.1',
    'description': 'Simple 13F Edgar Extractor',
    'long_description': None,
    'author': 'Ken Farr',
    'author_email': 'ken@farr.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
