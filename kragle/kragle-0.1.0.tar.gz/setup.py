# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['kragle']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'kragle',
    'version': '0.1.0',
    'description': 'glue and tape',
    'long_description': '# kragle\n',
    'author': 'Arni Inaba Kjartansson',
    'author_email': 'arni@inaba.is',
    'url': 'https://github.com/arni-inaba/kragle',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
