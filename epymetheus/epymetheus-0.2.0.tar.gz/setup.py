# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['epymetheus',
 'epymetheus._util',
 'epymetheus.datasets',
 'epymetheus.helper',
 'epymetheus.io',
 'epymetheus.old']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=0.25.3,<0.26.0']

setup_kwargs = {
    'name': 'epymetheus',
    'version': '0.2.0',
    'description': 'Python framework for multi-asset backtesting.',
    'long_description': None,
    'author': 'Shota Imaki',
    'author_email': 'shota.imaki@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
