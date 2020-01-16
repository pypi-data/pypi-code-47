# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['changelog_gen', 'changelog_gen.cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<7.1']

entry_points = \
{'console_scripts': ['changelog-gen = changelog_gen.cli.command:gen',
                     'changelog-init = changelog_gen.cli.command:init']}

setup_kwargs = {
    'name': 'changelog-gen',
    'version': '0.0.10',
    'description': 'Changelog generation tool',
    'long_description': "# Changelog Generator - v0.0.10\n\n## Installation\n\n```bash\npip install changelog-gen\n```\n\n## Notes\n\nCurrent python support 3.7, add 3.X and python 2.7 (or ignore cos EOL'd)\n",
    'author': 'Daniel Edgecombe',
    'author_email': 'edgy.edgemond@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/EdgyEdgemond/changelog-gen/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.8',
}


setup(**setup_kwargs)
