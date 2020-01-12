# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['homie_spec']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'homie-spec',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Xavier Francisco',
    'author_email': 'xavier.n.francisco@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
