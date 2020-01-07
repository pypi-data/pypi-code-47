# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['testpoetrypypi']

package_data = \
{'': ['*']}

install_requires = \
['poetry-version>=0.1.5,<0.2.0']

entry_points = \
{'console_scripts': ['runtest = runtest:main',
                     'testpoetrypypi = testpoetrypypi:main']}

setup_kwargs = {
    'name': 'testpoetrypypi',
    'version': '0.1.15',
    'description': '',
    'long_description': '# testpoetrypypi\nA reference-ish implementation of a Python project that uses:\n+ Poetry (and pyproject.toml)\n+ pytest and Black for testing and linting\n+ CircleCI\n+ Git Flow (i.e. `master` + `develop` + feature branches)\n+ [python-semantic-release](https://pypi.org/project/python-semantic-release/) to compute the next version and publish to PyPI upon merging `develop` into `master`.\n',
    'author': 'Jeff',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
