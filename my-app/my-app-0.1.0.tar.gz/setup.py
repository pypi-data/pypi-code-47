# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['my_app']

package_data = \
{'': ['*']}

install_requires = \
['django>=2.2,<4.0']

setup_kwargs = {
    'name': 'my-app',
    'version': '0.1.0',
    'description': 'Project template for Django app, using Poetry.',
    'long_description': '# Poetry Template\n\nDjango app template, using `poetry-python` as dependency manager.\n\nThis project is a template that can be cloned and re-used for redistributable apps.\n\nIt includes the following:\n\n* `poetry` for dependency management\n* `isort`, `black`, `pylint` and `flake8` linting\n* `pre-commit` to run linting\n* `mypy` for type checking\n* `tox` and `travis` for builds and CI\n\nThere are default config files for the linting and mypy.\n',
    'author': 'YunoJuno',
    'author_email': 'code@yunojuno.com',
    'maintainer': 'YunoJuno',
    'maintainer_email': 'code@yunojuno.com',
    'url': 'https://github.com/yunojuno/poetry-template',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
