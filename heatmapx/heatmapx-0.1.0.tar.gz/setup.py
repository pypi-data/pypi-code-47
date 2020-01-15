# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['heatmapx']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.1,<4.0', 'networkx>=2.4,<3.0']

setup_kwargs = {
    'name': 'heatmapx',
    'version': '0.1.0',
    'description': 'Flexible, intuitive heatmap creation on Network X graphs',
    'long_description': None,
    'author': 'drmrd',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
