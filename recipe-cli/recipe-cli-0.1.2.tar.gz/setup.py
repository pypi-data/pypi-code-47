# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['recipe_cli']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['recipe = recipe_cli:main']}

setup_kwargs = {
    'name': 'recipe-cli',
    'version': '0.1.2',
    'description': 'Recipe CLI tool',
    'long_description': '# Recipe-cli\n\nRecipe CLI tool',
    'author': 'Iman Kamyabi',
    'author_email': 'contact@imankamyabi.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://recipe.io',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
