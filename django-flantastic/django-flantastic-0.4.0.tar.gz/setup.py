# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flantastic',
 'flantastic.api',
 'flantastic.data',
 'flantastic.management',
 'flantastic.migrations',
 'flantastic.tests']

package_data = \
{'': ['*'],
 'flantastic': ['static/flantastic/css/*',
                'static/flantastic/icons/*',
                'static/flantastic/images/icons/*',
                'static/flantastic/js/*',
                'templates/flantastic/*'],
 'flantastic.management': ['commands/*']}

install_requires = \
['Django>=2.2,<3.0',
 'django-pwa>=1.0.5,<2.0.0',
 'pandas>=0.25.1,<0.26.0',
 'psycopg2>=2.8,<3.0',
 'requests>=2.22,<3.0',
 'tqdm>=4.36.1,<5.0.0']

setup_kwargs = {
    'name': 'django-flantastic',
    'version': '0.4.0',
    'description': 'GeoDjango app flantastic wich helps to find the best puddings.',
    'long_description': '# flantastic\n\n[![Build Status](https://travis-ci.org/Simarra/django-flantastic.svg?branch=develop)](https://travis-ci.org/Simarra/django-flantastic)\n\n[![PyPI version](https://badge.fury.io/py/django-flantastic.svg)](https://badge.fury.io/py/django-flantastic)\n\n\nAn app to found the best puddings of France!\n\n![cluster map example](.github/flantasticshot.jpg)\n\n\n## Purpose\nThis is a web application wich shows a map with points wich are bakeries. Each bakerie has notation based on some criterias, like taste, texture...\n\nThe votes of users are processed to color the points on the map and shown the "best" bakeries.\n\n## Installation\n- Python >=3.6\n- [Geodjango dependencies](https://docs.djangoproject.com/en/2.2/ref/contrib/gis/install/)\n\nStart a django app and then pip install django-flantastic.\n\nThen configure settings.py as you want, you can use postgis or Spatialite database as you wich.\n\nOptional setting are: \n- FLANTASTIC_CLOSEST_ITEMS_NB: *Choose how many items are shown each time user move the map*\n\n### Import initial data\nA script is ready to get bakeries from Christian Quest (Thank you!! ) geocoded SIRENE file data and import it into your database.\n\n```sh\npython manage.py migrate\npython manage.py import_initial_data\n\n\n\n',
    'author': 'Loic MARTEL',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Simarra/django-flantastic',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
