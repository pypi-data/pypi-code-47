# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['clii']
setup_kwargs = {
    'name': 'clii',
    'version': '0.1.0',
    'description': 'Function annotations -> argparse parser',
    'long_description': None,
    'author': "James O'Beirne",
    'author_email': 'james.obeirne@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
