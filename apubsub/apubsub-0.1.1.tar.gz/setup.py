# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['apubsub']

package_data = \
{'': ['*']}

extras_require = \
{':sys_platform == "linux"': ['uvloop>=0.14.0,<0.15.0']}

setup_kwargs = {
    'name': 'apubsub',
    'version': '0.1.1',
    'description': 'Message service implementing publisher/subscriber pattern',
    'long_description': "# apubsub\n\nSimple, single-purpose message service implementation.\n\n[![Build Status](https://travis-ci.org/outcatcher/apubsub.svg?branch=master)](https://travis-ci.org/outcatcher/apubsub)\n[![Coverage](https://codecov.io/gh/outcatcher/apubsub/branch/master/graph/badge.svg)](https://codecov.io/gh/outcatcher/apubsub)\n[![PyPI version](https://img.shields.io/pypi/v/apubsub.svg)](https://pypi.org/project/apubsub/)\n\n\n*Note that service is started in stand-alone process, so start it as early as possible to minimize resource pickling*\n\n### Installation\n\n_Python versin 3.7+ required_\n\nJust install it with pip: `pip install apubsub`\n\n### Usage\n\nThe most simple usage is to subscribe to topic and receive single message:\n\n```python\nfrom apubsub import Service\n\nservice = Service()\nservice.start()\n\npub = service.get_client()\nsub = service.get_client()  # every client can perform both pub and sub roles\n\nsub.subscribe('topic')\n\npub.publish('topic', 'some data')  # publish put data to subscribed Client queue\n\npub.publish('topic', 'some more data')\npub.publish('topic', 'and more')\n\ndata = sub.get_single(timeout=0.1)  # 'some data'\n\ndata = sub.get_all()  # ['some more data', 'and more']\n\n```\n\nAlso, `Client` provides `start_receiving` async generator for receiving messages on-demand.\nIt will wait for new messages until interrupted by `stop_receiving` call\n",
    'author': 'Anton Kachurin',
    'author_email': 'katchuring@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/outcatcher/apubsub',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
