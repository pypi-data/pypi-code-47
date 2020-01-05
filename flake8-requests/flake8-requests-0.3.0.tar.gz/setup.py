# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flake8_requests']

package_data = \
{'': ['*']}

install_requires = \
['flake8>=3.7.9,<4.0.0', 'r2c-py-ast==0.1.0b1']

entry_points = \
{'flake8.extension': ['r2c-requests = flake8_requests.main:Flake8Requests']}

setup_kwargs = {
    'name': 'flake8-requests',
    'version': '0.3.0',
    'description': 'Checks for the requests module, by r2c. Available in [Bento](https://bento.dev).',
    'long_description': '\n# flake8-requests\n\nflake8-requests is a plugin for flake8 with checks specifically for the [request](https://pypi.org/project/requests/) framework.\n\n## Installation\n\n```\npip install flake8-requests\n```\n\nValidate the install using `--version`. flake8-requests adds two plugins, but this will be consolidated in a very near-future version. :)\n\n```\n> flake8 --version\n3.7.9 (mccabe: 0.6.1, pycodestyle: 2.5.0, pyflakes: 2.1.1, flake8-requests)\n```\n\n## List of warnings\n- `r2c-requests-no-auth-over-http`: Alerts when `auth` param is possibly used over http://, which could expose credentials. See more documentation at https://checks.bento.dev/en/latest/flake8-requests/r2c-requests-no-auth-over-http/\n- `r2c-requests-use-scheme`: Alerts when URLs passed to  `requests` API methods dont have a URL scheme (e.g., https://), otherwise an exception will be thrown. See more documentation at\nhttps://checks.bento.dev/en/latest/flake8-requests/r2c-requests-use-scheme/\n',
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
