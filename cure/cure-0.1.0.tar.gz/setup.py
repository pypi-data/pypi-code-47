# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['cure']

package_data = \
{'': ['*']}

install_requires = \
['decorator>=4.4.1,<5.0.0']

setup_kwargs = {
    'name': 'cure',
    'version': '0.1.0',
    'description': 'Decorator for fixing naming conventions to keys of keyword arguments - adds trailing underscores to keys using bad naming such as reserved keywords or Python built-ins',
    'long_description': '# `cure`\n[![pypi](https://badge.fury.io/py/cure.svg)](https://pypi.python.org/pypi/cure/)\n[![Made with Python](https://img.shields.io/pypi/pyversions/cure)](https://www.python.org/)\n[![Type hinted - mypy validated](https://img.shields.io/badge/typehinted-yes-teal)](https://github.com/kalaspuff/cure)\n[![MIT License](https://img.shields.io/github/license/kalaspuff/cure.svg)](https://github.com/kalaspuff/cure/blob/master/LICENSE)\n[![Code coverage](https://codecov.io/gh/kalaspuff/cure/branch/master/graph/badge.svg)](https://codecov.io/gh/kalaspuff/cure/tree/master/cure)\n\n*Library for adding trailing underscores to passed down keyword arguments from third party libraries. Adds the preferred trailing underscore to the key in the kwarg if the key would conflict with the Python reserved keywords or Python built-ins. Methods can be decorated with the `@cure` decorator.*\n\n\n## Installation with `pip`\nLike you would install any other Python package, use `pip`, `poetry`, `pipenv` or your weapon of choice.\n```\n$ pip install cure\n```\n\n\n## Usage and examples\n\n#### `@cure` decorator\n',
    'author': 'Carl Oscar Aaro',
    'author_email': 'hello@carloscar.com',
    'url': 'https://github.com/kalaspuff/cure',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
