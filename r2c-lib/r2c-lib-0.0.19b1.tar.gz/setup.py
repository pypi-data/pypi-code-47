# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['r2c', 'r2c.lib', 'r2c.lib.analysis', 'r2c.lib.schemas', 'r2c.lib.tests']

package_data = \
{'': ['*']}

install_requires = \
['cattrs>=0.9.0,<0.10.0',
 'docker>=3.7,<4.0',
 'gitpython>=2.1,<3.0',
 'importlib_resources>=1.0,<2.0',
 'jsondiff>=1.1,<2.0',
 'jsonschema>=3.0,<4.0',
 'mypy-extensions>=0.4,<0.5',
 'requests>=2.0,<3.0',
 'semantic-version>=2.7,<3.0',
 'toposort>=1.5,<2.0']

setup_kwargs = {
    'name': 'r2c-lib',
    'version': '0.0.19b1',
    'description': 'Supporting libraries for R2C',
    'long_description': '# r2c.lib\n\nThis publicly-distributable library contains supporting functionality\nfor shared R2C components.\n',
    'author': 'R2C',
    'author_email': 'cli@ret2.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://ret2.co',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
