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

install_requires = \
['psycopg2>=2.8.4,<3.0.0']

setup_kwargs = {
    'name': 'tenark',
    'version': '0.6.0',
    'description': '',
    'long_description': None,
    'author': 'Esteban Echeverry',
    'author_email': 'eecheverry@nubark.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
