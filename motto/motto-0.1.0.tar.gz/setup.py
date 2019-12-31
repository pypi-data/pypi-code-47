# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['motto', 'motto.core', 'motto.skills']

package_data = \
{'': ['*']}

install_requires = \
['click-default-group>=1.2.2,<2.0.0',
 'click>=7.0,<8.0',
 'docutils>=0.15.2,<0.16.0',
 'janome>=0.3.10,<0.4.0',
 'typing-extensions>=3.7.4,<4.0.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses>=0.7,<0.8']}

entry_points = \
{'console_scripts': ['motto = motto.cli:main']}

setup_kwargs = {
    'name': 'motto',
    'version': '0.1.0',
    'description': 'Japanese document Analytics Machine',
    'long_description': None,
    'author': 'Kazuya Takei',
    'author_email': 'attakei@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
