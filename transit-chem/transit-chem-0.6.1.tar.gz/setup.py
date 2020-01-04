# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['transit_chem']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=19.3,<20.0',
 'cattrs>=1.0,<2.0',
 'click>=7.0,<8.0',
 'joblib>=0.14.1,<0.15.0',
 'loguru>=0.4.0,<0.5.0',
 'matplotlib>=3.1,<4.0',
 'numba>=0.43.0,<0.44.0',
 'numpy>=1.17,<2.0',
 'scipy>=1.3,<2.0',
 'tqdm>=4.39,<5.0']

entry_points = \
{'console_scripts': ['transit-chem = transit_chem.cli:cli']}

setup_kwargs = {
    'name': 'transit-chem',
    'version': '0.6.1',
    'description': 'Quantifying Probabilistic Electron Transit times.',
    'long_description': 'transit-chem\n============\n\n\n.. image:: https://img.shields.io/pypi/v/transit_chem.svg\n        :target: https://pypi.python.org/pypi/transit_chem\n\n\n.. image:: https://readthedocs.org/projects/transit-chem/badge/?version=latest\n        :target: https://transit-chem.readthedocs.io/en/latest/?badge=latest\n        :alt: Documentation Status\n\n\nQuantifying electron transit in donor-bridge-acceptor systems using probabilistic confidence.\n\n\n* Free software: MIT license\n* Documentation: https://transit-chem.readthedocs.io.\n\n\nFeatures\n--------\n',
    'author': 'Evan Curtin',
    'author_email': 'fakeemail@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
