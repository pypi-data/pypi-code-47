# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fracdiff']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.18.0,<2.0.0',
 'scikit-learn>=0.22.1,<0.23.0',
 'statsmodels>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'fracdiff',
    'version': '0.0.3',
    'description': 'Fractional differentiation of time-series.',
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
