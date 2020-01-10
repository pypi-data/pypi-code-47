# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lms_prepaid']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'requests>=2.22.0,<3.0.0', 'tritise>=0.1.0,<0.2.0']

entry_points = \
{'console_scripts': ['lms-prepaid = lms_prepaid.lms_prepaid:query']}

setup_kwargs = {
    'name': 'lms-prepaid',
    'version': '0.1.0',
    'description': 'A script to query Last Mile Solutions prepaid card values',
    'long_description': None,
    'author': 'asmw',
    'author_email': 'asmw@asmw.org',
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
