# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deepehr']

package_data = \
{'': ['*']}

install_requires = \
['gensim>=3.8.1,<4.0.0',
 'ipykernel>=5.1.3,<6.0.0',
 'pandas>=0.25.3,<0.26.0',
 'seaborn>=0.9.0,<0.10.0',
 'torch>=1.3.1,<2.0.0']

setup_kwargs = {
    'name': 'deepehr',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'yajiez',
    'author_email': 'yajiez.me@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
