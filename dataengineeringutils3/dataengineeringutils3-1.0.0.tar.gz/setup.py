# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['dataengineeringutils3']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.10,<2.0']

setup_kwargs = {
    'name': 'dataengineeringutils3',
    'version': '1.0.0',
    'description': 'Data engineering utils python 3 version',
    'long_description': '[![Coverage Status](https://coveralls.io/repos/github/moj-analytical-services/dataengineeringutils3/badge.svg?branch=master)](https://coveralls.io/github/moj-analytical-services/dataengineeringutils3?branch=master)\n\n# Data engineering utils - Python 3\n\nFully unit tested utility functions for data engineering. Python 3 only.  \n\n\n## Installation\n\n```bash\npip install dataengineeringutils3\n```\n\n\n## Testing\n\n```bash\npytest --cov-report term-missing --cov=dataengineeringutils3 tests/\n```\n',
    'author': 'Josh Rowe',
    'author_email': 'josh.rowe@digital.justice.gov.uk',
    'url': 'https://github.com/moj-analytical-services/dataengineeringutils3',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
