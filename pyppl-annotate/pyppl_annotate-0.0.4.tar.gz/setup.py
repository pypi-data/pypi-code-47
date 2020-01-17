# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pyppl_annotate']
install_requires = \
['pyppl>=3.0.0,<4.0.0']

entry_points = \
{'pyppl': ['pyppl_annotate = pyppl_annotate']}

setup_kwargs = {
    'name': 'pyppl-annotate',
    'version': '0.0.4',
    'description': 'Adding long description/annotations for PyPPL processes.',
    'long_description': None,
    'author': 'pwwang',
    'author_email': 'pwwang@pwwang.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
