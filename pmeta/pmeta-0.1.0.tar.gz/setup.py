# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pmeta']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pmeta',
    'version': '0.1.0',
    'description': 'Python for Meta Analysis',
    'long_description': None,
    'author': 'Yajie Zhu',
    'author_email': 'yajiez.me@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
