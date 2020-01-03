# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_demo']

package_data = \
{'': ['*']}

install_requires = \
['pendulum>=2.0.5,<3.0.0']

setup_kwargs = {
    'name': 'poetry-demo',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Shabie Iqbal',
    'author_email': 'shabieiqbal@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)
