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
    'version': '1.0.0',
    'description': 'HTTP server over SSL/TLS with an automatically generated self-signed certificate',
    'long_description': '# httpself\n\nHTTP server over SSL/TLS with an automatically generated self-signed certificate.\n\n## Usage\n\nServe static files from the current working directory:\n\n```shell\n$ https [-p/--port <NNNN>] [--public]\n```\n\n### Example #1\n\nBy default, the server runs on port number `443`, which requires superuser privileges. Note that the server will only be accessible from the `localhost`:\n\n```shell\n$ https\nRunning server at https://localhost:443\n```\n\n### Example #2\n\nTo specify an alternative port number:\n\n```shell\n$ https --port 8443\nRunning server at https://localhost:8443\n```\n\n### Example #3\n\nTo make the server accessible from other devices:\n\n```shell\n$ https --public\nRunning server at https://0.0.0.0:443\n```\n\n### Example #4\n\nTo run the server publicly on a custom port:\n\n```shell\n$ https --public -p 8443\nRunning server at https://0.0.0.0:8443\n```\n\n## Installation\n\n```shell\n$ pip install httpself\n```\n',
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
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
