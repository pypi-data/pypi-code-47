# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['caterpie', 'caterpie.postgresql']

package_data = \
{'': ['*'], 'caterpie': ['sqlite/*']}

install_requires = \
['configparser>=4.0.2,<5.0.0',
 'pandas>=0.25.3,<0.26.0',
 'python-dotenv>=0.10.3,<0.11.0']

setup_kwargs = {
    'name': 'caterpie',
    'version': '0.1.0',
    'description': 'Lightweight ORM for uploading CSV files to a relational database.',
    'long_description': None,
    'author': 'smk508',
    'author_email': 'skhan8@mail.einstein.yu.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
