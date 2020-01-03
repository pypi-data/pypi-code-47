# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['fastapi_etag']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fastapi-etag',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Steinthor Palsson',
    'author_email': 'steini90@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
