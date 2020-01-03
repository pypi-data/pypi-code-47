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
    'version': '0.1.2',
    'description': '',
    'long_description': '`poetry install`\n`poetry run pytest`\n`poetry run testpoetrypypi`\n`poetry run semantic-release version --noop`\n',
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
