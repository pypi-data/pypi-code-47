# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tenark',
 'tenark.cataloguer',
 'tenark.common',
 'tenark.identifier',
 'tenark.models',
 'tenark.provisioner']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tenark',
    'version': '0.4.0',
    'description': '',
    'long_description': None,
    'author': 'Esteban Echeverry',
    'author_email': 'eecheverry@nubark.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
