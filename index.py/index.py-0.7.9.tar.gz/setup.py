# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['index', 'index.openapi']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=0.4.0,<0.5.0',
 'gunicorn>=20.0.4,<21.0.0',
 'jinja2>=2.10.3,<3.0.0',
 'pydantic>=1.3,<2.0',
 'python-multipart>=0.0.5,<0.0.6',
 'pyyaml>=5.3,<6.0',
 'requests>=2.22.0,<3.0.0',
 'starlette>=0.13.0,<0.14.0',
 'uvicorn>=0.11.1,<0.12.0',
 'watchdog>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['index-cli = index.cli:main']}

setup_kwargs = {
    'name': 'index.py',
    'version': '0.7.9',
    'description': 'An easy-to-use asynchronous web framework based on ASGI.',
    'long_description': None,
    'author': 'abersheeran',
    'author_email': 'me@abersheeran.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/abersheeran/index.py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
