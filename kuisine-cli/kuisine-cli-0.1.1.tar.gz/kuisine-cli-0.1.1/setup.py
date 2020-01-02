# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kuisine']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'requests>=2.22.0,<3.0.0']

setup_kwargs = {
    'name': 'kuisine-cli',
    'version': '0.1.1',
    'description': 'Command line interface for kuisine.ru',
    'long_description': '\n[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg?style=flat)](https://www.python.org/downloads/)\n[![PyPI](https://img.shields.io/pypi/v/kuisine-cli.svg)](https://pypi.org/project/kuisine-cli/)\n[![Build Status](https://github.com/yafeunteun/kuisine-cli/workflows/CI/badge.svg)](https://github.com/yafeunteun/kuisine-cli/actions)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n\n\n## Dev\n\n### Add pre-commit hooks \nWe use pre commit hooks to run automatically `black` and `mypy` on commit.\n\nrun `poetry run pre-commit install` to set up the git hooks script\n\n\n## Licenses\n\nkuisine-cli is released under the [MIT license](https://github.com/yafeunteun/kuisine-cli/blob/master/LICENSE).\n',
    'author': 'Yann Feunteun',
    'author_email': 'yann.feunteun@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/yafeunteun/kuisine-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
