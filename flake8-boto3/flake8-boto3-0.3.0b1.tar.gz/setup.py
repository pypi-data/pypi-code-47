# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flake8_boto3']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.10.21,<2.0.0', 'flake8>=3.7.9,<4.0.0', 'r2c-py-ast==0.1.0b1']

entry_points = \
{'flake8.extension': ['r2c-boto3 = flake8_boto3.main:Flake8Boto3']}

setup_kwargs = {
    'name': 'flake8-boto3',
    'version': '0.3.0b1',
    'description': 'Checks for boto3, by r2c. Available in [Bento](https://bento.dev).',
    'long_description': '# flake8-boto3\n\nflake8-boto3 is a plugin for flake8 with checks specifically for [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), written by [r2c](https://r2c.dev). This plugin is available by default in our program analysis tool, [Bento](https://bento.dev).\n\n## Installation\n\n```\npip install flake8-boto3\n```\n\nValidate the install using `flake8 --version`.\n\n```\n> flake8 --version\n3.7.9 (flake8-boto3: 0.2.2, mccabe: 0.6.1, pycodestyle: 2.5.0, pyflakes: 2.1.1)\n```\n\n## List of Warnings\n\n`r2c-boto3-hardcoded-access-token`: This check detects the use of a hardcoded access token for any of the `aws_access_key_id`, `aws_secret_access_key`, `aws_session_token` keyword arguments.',
    'author': 'R2C',
    'author_email': 'hello@returntocorp.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://bento.dev',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
