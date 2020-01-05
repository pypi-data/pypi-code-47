# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['repacolors']

package_data = \
{'': ['*'], 'repacolors': ['command/*']}

install_requires = \
['click>=7.0,<8.0']

entry_points = \
{'console_scripts': ['repacolor = repacolors.command.repacolor:color']}

setup_kwargs = {
    'name': 'repacolors',
    'version': '0.1.0',
    'description': 'Small library for color conversion, manipulation, etc.',
    'long_description': '# repacolors\n\nSmall library for color conversion, manipulation, etc.\n',
    'author': 'Gyuri Horak',
    'author_email': 'dyuri@horak.hu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
