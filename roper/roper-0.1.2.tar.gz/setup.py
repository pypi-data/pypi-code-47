# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['roper']

package_data = \
{'': ['*']}

install_requires = \
['invoke>=1.3.0,<2.0.0', 'rope>=0.14.0,<0.15.0']

entry_points = \
{'console_scripts': ['roper = roper.__main__:program.run']}

setup_kwargs = {
    'name': 'roper',
    'version': '0.1.2',
    'description': 'A CLI tool for the roper library.',
    'long_description': '=====\nroper\n=====\n\nA CLI tool for the roper library.\n\nDevelop\n=======\nThis package was setup using https://python-poetry.org/. To get started, install poetry\n(`pip install --user poetry`), run `poetry install` in the project directory and enter the\nvirtualenv by running `poetry shell`.\n\nAlternatives\n============\n\nIDEs\n----\n* PyCharm - https://www.jetbrains.com/help/pycharm/refactoring-source-code.html\n\nEditor plugins\n--------------\n* vim - https://github.com/python-rope/ropevim\n* emacs - https://github.com/python-rope/ropemacs\n\nLibraries\n---------\n* bowler - https://pybowler.io/\n* libcst - https://libcst.readthedocs.io/en/latest/\n* undebt - https://github.com/Yelp/undebt\n* redbaron - http://redbaron.pycqa.org/en/latest/\n\nResources\n=========\n* https://realpython.com/python-refactoring/\n',
    'author': 'Øystein S. Haaland',
    'author_email': 'oystein@beat.no',
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
