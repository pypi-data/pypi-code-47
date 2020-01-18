# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_shell', 'pytest_shell.tests']

package_data = \
{'': ['*']}

entry_points = \
{'pytest11': ['shell = pytest_shell']}

setup_kwargs = {
    'name': 'pytest-shell',
    'version': '0.2.2',
    'description': 'A pytest plugin for testing shell scripts and line-based processes',
    'long_description': None,
    'author': 'Daniel Murray',
    'author_email': 'daniel@darkdisco.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://hg.sr.ht/~danmur/pytest-shell',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
