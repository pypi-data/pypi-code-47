# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['timeflake']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'timeflake',
    'version': '0.1.0',
    'description': 'Timeflakes are 64-bit roughly-ordered, globally-unique, URL-safe UUIDs.',
    'long_description': None,
    'author': 'Anthony Najjar Simon',
    'author_email': 'anthonynsimon@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
