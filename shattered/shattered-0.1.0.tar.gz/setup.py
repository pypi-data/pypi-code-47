# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['shattered']

package_data = \
{'': ['*']}

install_requires = \
['stomp.py>=5.0.0,<6.0.0']

setup_kwargs = {
    'name': 'shattered',
    'version': '0.1.0',
    'description': 'STOMP meets bottle.py',
    'long_description': None,
    'author': 'Jimmy Bradshaw',
    'author_email': 'james.g.bradshaw@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
