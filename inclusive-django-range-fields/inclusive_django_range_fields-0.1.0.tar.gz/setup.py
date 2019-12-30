# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['inclusive_django_range_fields', 'inclusive_django_range_fields.drf']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'inclusive-django-range-fields',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Hipo',
    'author_email': 'pypi@hipolabs.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)
