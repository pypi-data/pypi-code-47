# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['russe_pack']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'lxml>=4.4.2,<5.0.0',
 'requests>=2.22.0,<3.0.0',
 'selenium>=3.141.0,<4.0.0']

entry_points = \
{'console_scripts': ['get_russianpodcasts = russe_pack.get_episodes:main']}

setup_kwargs = {
    'name': 'russe-pack',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Colin Goutte',
    'author_email': 'cgte@bk.ru',
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
