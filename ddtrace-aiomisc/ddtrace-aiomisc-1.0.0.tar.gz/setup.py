# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ddtrace_aiomisc']

package_data = \
{'': ['*']}

install_requires = \
['ddtrace>=0.31,<0.32']

setup_kwargs = {
    'name': 'ddtrace-aiomisc',
    'version': '1.0.0',
    'description': 'ddtrace miscellaneous utils',
    'long_description': '# ddtrace-aiomisc\n\nddtrace miscellaneous utils\n',
    'author': 'm.shlyamov',
    'author_email': 'm.shlyamov@yandex.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SandLabs/ddtrace-aiomisc',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
