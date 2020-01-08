# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['httpself']

package_data = \
{'': ['*']}

install_requires = \
['pyopenssl>=19.1.0,<20.0.0']

entry_points = \
{'console_scripts': ['https = httpself.cli:run']}

setup_kwargs = {
    'name': 'httpself',
    'version': '0.1.0',
    'description': 'HTTP server over SSL/TLS with an automatically generated self-signed certificate',
    'long_description': '# httpself\n\nHTTP server over SSL/TLS with an automatically generated self-signed certificate.\n\n## Usage\n\nServe static files from the current working directory:\n\n```shell\n$ https [-p/--port <NNNN>] [--public]\n```\n\n### Example #1\n\nBy default, the server runs on port number `443`, which requires superuser privileges. Note that the server will only be accessible from the `localhost`:\n\n```shell\n$ https\n```\n\n### Example #2\n\nTo specify an alternative port number:\n\n```shell\n$ https --port 8443\n```\n\n### Example #3\n\nTo make the server accessible from other devices:\n\n```shell\n$ https --public\n```\n\n## Installation\n\n### PyPI\n\n```shell\n$ pip install httpself\n```\n\n### Source Code\n\nDownload the source code:\n\n```shell\n$ git clone git@github.com:bzaczynski/httpself.git\n```\n\nInstall [poetry](https://poetry.eustace.io/):\n\n```shell\n$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python\n```\n\nInstall the module after download:\n\n```shell\n$ cd httpself/\n$ poetry install\n```\n\nUse poetry to run the server:\n\n```shell\n$ poetry run https\n```\n',
    'author': 'Bartosz Zaczyński',
    'author_email': 'bartosz.zaczynski@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bzaczynski/httpself',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
