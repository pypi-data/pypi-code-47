# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['labthings',
 'labthings.consumer',
 'labthings.core',
 'labthings.core.tasks',
 'labthings.server',
 'labthings.server.spec',
 'labthings.server.views',
 'labthings.server.views.docs']

package_data = \
{'': ['*'],
 'labthings.server': ['views/docs/static/*', 'views/docs/templates/*']}

install_requires = \
['Flask>=1.1.1,<2.0.0',
 'apispec>=3.2.0,<4.0.0',
 'flask-cors>=3.0.8,<4.0.0',
 'marshmallow>=3.3.0,<4.0.0',
 'webargs>=5.5.2,<6.0.0']

setup_kwargs = {
    'name': 'labthings',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'jtc42',
    'author_email': 'jtc9242@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
