# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hashversion']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'gitpython>=3.0.5,<4.0.0', 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['hashver = hashver:cli']}

setup_kwargs = {
    'name': 'hashversion',
    'version': '0.1.0',
    'description': 'Automate versioning and related requirements when using hashver',
    'long_description': '# Hash Version\n\n![License](https://img.shields.io/github/license/miniscruff/hashversion-python.svg)\n![Issues](https://img.shields.io/github/issues/miniscruff/hashversion-python.svg)\n\nPython CLI for automating hash versioning and related requirements.\nTo help automate versioning, changelog management and other pieces of continuous\ndeployments.\n\n## Installation :inbox_tray:\n```bash\n> git clone https://github.com/miniscruff/hashversion-python.git\n> cd  hashver-python\n> poetry install\n> pytest\n> black .\n```\n\n## Bugs :bug:\n\nThis project is getting upgrades in my free time if there is a problem please create a bug report in the issues section.\n\n## License :scroll:\n\n- Licensed under [MIT License](https://github.com/miniscruff/hashversion-python/blob/master/LICENSE)\n',
    'author': 'Ronnie Smith',
    'author_email': 'halfpint1170@gmail.com',
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
