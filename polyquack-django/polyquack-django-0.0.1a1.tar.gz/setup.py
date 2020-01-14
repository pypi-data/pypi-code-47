# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['polyquack_django']

package_data = \
{'': ['*']}

install_requires = \
['Django>2.2,<4', 'polyquack>=0.2,<0.3']

setup_kwargs = {
    'name': 'polyquack-django',
    'version': '0.0.1a1',
    'description': 'Placeholder package to reserve name - do not use',
    'long_description': '# polyquack-django\n\npolyquack translation and pluralization utilities and fields for Django.',
    'author': 'Patryk Bratkowski',
    'author_email': 'git@patryk.tech',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/patryk-media/polyquack',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
