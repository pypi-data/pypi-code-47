# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sql2json', 'sql2json.parameter']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.3.12,<2.0.0',
 'fire>=0.2.1,<0.3.0',
 'python-dateutil>=2.8.1,<3.0.0']

setup_kwargs = {
    'name': 'sql2json',
    'version': '0.1.7',
    'description': 'Tool to run a SQL query a convert result to JSON',
    'long_description': None,
    'author': 'Francisco Perez',
    'author_email': 'fsistemas@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fsistemas/sql2json',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
