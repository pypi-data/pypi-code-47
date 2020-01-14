# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dynatademand']

package_data = \
{'': ['*'],
 'dynatademand': ['schemas/request/body/*',
                  'schemas/request/path/*',
                  'schemas/request/query/*']}

install_requires = \
['jsonschema==3.2.0',
 'pytest-runner==5.2',
 'pytest==4.6.6',
 'requests==2.22.0',
 'responses==0.10.6']

setup_kwargs = {
    'name': 'dynatademand',
    'version': '1.0.2',
    'description': 'A Python client library for the Dynata Demand API',
    'long_description': None,
    'author': 'Ridley Larsen',
    'author_email': 'Ridley.Larsen@dynata.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
