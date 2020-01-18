# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['netizenship']
install_requires = \
['beautifulsoup4>=4.8.2,<5.0.0',
 'pyfiglet>=0.8.post1,<0.9',
 'requests>=2.22.0,<3.0.0',
 'termcolor>=1.1.0,<2.0.0']

entry_points = \
{'console_scripts': ['netizenship = netizenship:main']}

setup_kwargs = {
    'name': 'netizenship',
    'version': '0.1.5',
    'description': 'Tool to check the username with popular websites for membership',
    'long_description': None,
    'author': 'Rahul Raj',
    'author_email': 'rahulrajpl@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
