# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['slskit']

package_data = \
{'': ['*']}

install_requires = \
['colorlog>=4.1.0,<5.0.0',
 'funcy>=1.14,<2.0',
 'jsonschema>=3.2.0,<4.0.0',
 'pyyaml>=5.1,<6.0',
 'salt>=2019.2,<2020.0']

entry_points = \
{'console_scripts': ['slskit = slskit:run_module']}

setup_kwargs = {
    'name': 'slskit',
    'version': '2020.1.3',
    'description': 'Tools for checking Salt state validity',
    'long_description': '# slskit\n\n![black](https://img.shields.io/badge/code%20style-black-000000.svg)\n\n```\nusage: slskit [-h] [-c CONFIG] {highstate,pillars,refresh} ...\n\nslskit - tools for checking Salt state validity\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -c CONFIG, --config CONFIG\n                        path to slskit configuration file (default:\n                        slskit.yaml or slskit.yml)\n\ncommands:\n  {highstate,pillars,refresh}\n    highstate           renders the states for the specified minions\n    pillars             renders pillar items for the specified minions\n    refresh             invokes saltutil.sync_all runner\n```\n',
    'author': 'Gediminas Zlatkus',
    'author_email': 'gediminas.zlatkus@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gediminasz/slskit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
