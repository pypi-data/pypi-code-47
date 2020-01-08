# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['goldenmask']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0']

entry_points = \
{'console_scripts': ['goldenmask = goldenmask.cli:goldenmask']}

setup_kwargs = {
    'name': 'goldenmask',
    'version': '0.1.2',
    'description': 'Protect your python source code with one command.',
    'long_description': '# goldenmask\n\nProtect your python source code with one command.',
    'author': 'youngquan',
    'author_email': 'youngquan@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/youngquan/goldenmask',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
