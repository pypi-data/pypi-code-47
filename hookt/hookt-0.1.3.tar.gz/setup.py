# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['hookt']
install_requires = \
['anyio>=1.2.3,<2.0.0', 'wrapt>=1.11.2,<2.0.0']

setup_kwargs = {
    'name': 'hookt',
    'version': '0.1.3',
    'description': 'Asynchronous function hooks using decorators.',
    'long_description': '`hookt` is an asynchronous event framework utilizing decorators.\nIt uses anyio, so it is compatible with `asyncio`, `curio` and `trio`.\nFor an up-to-date list of compatible backends,\nsee [`anyio`](https://github.com/agronholm/anyio)\n\n## installation\n`pip install hookt`\n',
    'author': 'nanananisore',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nanananisore/hookt',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
