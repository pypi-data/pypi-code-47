# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['openstates_metadata', 'openstates_metadata.data', 'openstates_metadata.tests']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=19.3,<20.0', 'pyyaml>=5.3,<6.0', 'us>=1.0,<2.0']

setup_kwargs = {
    'name': 'openstates-metadata',
    'version': '2020.1.16',
    'description': 'metadata for the openstates project',
    'long_description': '# metadata\n\nThis repository contains state metadata that powers Open States.\n\n[![CircleCI](https://circleci.com/gh/openstates/metadata.svg?style=svg)](https://circleci.com/gh/openstates/metadata)\n\n## Links\n\n* [Open States Discourse](https://discourse.openstates.org)\n* [Code of Conduct](https://docs.openstates.org/en/latest/contributing/code-of-conduct.html)\n',
    'author': 'James Turk',
    'author_email': 'james@openstates.org',
    'url': 'https://github.com/openstates/metadata',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
