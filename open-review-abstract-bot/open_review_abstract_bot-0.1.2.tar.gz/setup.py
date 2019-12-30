# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['open_review_abstract_bot']

package_data = \
{'': ['*']}

install_requires = \
['attr>=0.3.1,<0.4.0',
 'beautifulsoup4>=4.8.2,<5.0.0',
 'html2text>=2019.9.26,<2020.0.0',
 'praw>=6.4.0,<7.0.0',
 'requests>=2.22.0,<3.0.0',
 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['openreviewbot = open_review_abstract_bot.console:run']}

setup_kwargs = {
    'name': 'open-review-abstract-bot',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'Stelios Tymvios',
    'author_email': 'solliet@protonmail.com',
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
