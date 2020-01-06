# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_localizer',
 'django_localizer.management',
 'django_localizer.management.commands',
 'django_localizer.templatetags']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.0.1,<4.0.0', 'stew>=0.1.2,<0.2.0']

setup_kwargs = {
    'name': 'django-localizer',
    'version': '0.1.4',
    'description': 'A library for making localizing django apps easier',
    'long_description': None,
    'author': 'Timofey Danshin',
    'author_email': 't.danshin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
