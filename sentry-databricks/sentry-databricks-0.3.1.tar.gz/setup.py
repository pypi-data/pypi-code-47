# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sentry_databricks', 'sentry_databricks.notebook']

package_data = \
{'': ['*']}

install_requires = \
['sentry-sdk>=0.13.0,<0.14.0']

setup_kwargs = {
    'name': 'sentry-databricks',
    'version': '0.3.1',
    'description': '',
    'long_description': None,
    'author': 'Jiri Koutny',
    'author_email': 'jiri.koutny@datasentics.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DataSentics/sentry-databricks',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5.2',
}


setup(**setup_kwargs)
