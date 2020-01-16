# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neuralbandit']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.18.1,<2.0.0', 'pandas>=0.25.3,<0.26.0', 'torch>=1.4.0,<2.0.0']

setup_kwargs = {
    'name': 'neuralbandit',
    'version': '0.1.1',
    'description': 'Reproducing the experiments of the NeuralBandit and BanditForest papers. ',
    'long_description': None,
    'author': 'rallesiardo',
    'author_email': 'robin.allesiardo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
