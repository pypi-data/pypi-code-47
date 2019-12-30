# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'Package'}

packages = \
['synodic_tools']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'gitpython>=3.0.3,<4.0.0',
 'semantic_version>=2.8.2,<3.0.0',
 'synodic-poetry>=0.1,<0.2']

entry_points = \
{'console_scripts': ['synodic = synodic_tools.app:entrypoint']}

setup_kwargs = {
    'name': 'synodic-tools',
    'version': '0.1.0',
    'description': ' A Python library to provide tooling support for the majority of Synodic software.',
    'long_description': '# Synodic Tools\n',
    'author': 'Synodic Software',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Synodic-Software/Synodic-Tools',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
