# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['melange',
 'melange.domain_event_bus',
 'melange.drivers',
 'melange.drivers.aws',
 'melange.infrastructure',
 'melange.messaging']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.11.5,<2.0.0',
 'marshmallow>=3.3.0,<4.0.0',
 'pika>=1.1.0,<2.0.0',
 'pyopenssl>=19.1.0,<20.0.0',
 'redis-simple-cache-py3>=0.0.7,<0.0.8']

setup_kwargs = {
    'name': 'melange',
    'version': '4.3.0',
    'description': 'A messaging library for an easy inter-communication in distributed and microservices architectures',
    'long_description': None,
    'author': 'David Jim\xc3\xa9nez (Rydra)',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
