# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['changelog_gen', 'changelog_gen.cli']

package_data = \
{'': ['*']}

install_requires = \
['bump2version>=0.5.11,<0.6.0', 'click>=7.0,<8.0']

entry_points = \
{'console_scripts': ['changelog-gen = changelog_gen.cli.command:gen',
                     'changelog-init = changelog_gen.cli.command:init']}

setup_kwargs = {
    'name': 'changelog-gen',
    'version': '0.2.2',
    'description': 'Changelog generation tool',
    'long_description': "# Changelog Generator - v0.2.2\n\n## Installation\n\n```bash\npip install changelog-gen\n```\n\n## Notes\n\nCurrent python support 3.7, add 3.X and python 2.7 (or ignore cos EOL'd)\n\n```bash\n$ changelog-gen\n\n## v0.2.2\n\n### Bug fixes\n\n- Raise errors from internal classes, don't use click.echo() [#4]\n\n- Update changelog line format to include issue number at the end. [#7]\n\nWrite CHANGELOG for suggested version 0.2.2 [y/N]: y\n```\n",
    'author': 'Daniel Edgecombe',
    'author_email': 'edgy.edgemond@gmail.com',
    'url': 'https://github.com/EdgyEdgemond/changelog-gen/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.8',
}


setup(**setup_kwargs)
