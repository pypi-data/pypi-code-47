# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['extra_qt', 'extra_qt.dom', 'extra_qt.renderers']

package_data = \
{'': ['*']}

install_requires = \
['PyQt5>=5.14.1,<6.0.0']

setup_kwargs = {
    'name': 'extra-qt',
    'version': '0.1.0',
    'description': 'React-like bindings for PyQt5 without JavaScript.',
    'long_description': None,
    'author': 'Conrad Stansbury',
    'author_email': 'chstansbury@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
