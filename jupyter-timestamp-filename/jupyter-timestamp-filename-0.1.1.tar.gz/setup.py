# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jupyter_timestamp_filename']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'jupyter-timestamp-filename',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'fx_kirin',
    'author_email': 'fx.kirin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
