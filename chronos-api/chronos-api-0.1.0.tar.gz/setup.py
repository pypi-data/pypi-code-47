# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['chronos']

package_data = \
{'': ['*']}

install_requires = \
['flask>=1.1.1,<2.0.0',
 'google-api-python-client>=1.7.11,<2.0.0',
 'google-auth-httplib2>=0.0.3,<0.0.4',
 'google-auth-oauthlib>=0.4.1,<0.5.0',
 'gunicorn>=20.0.4,<21.0.0',
 'iso8601>=0.1.12,<0.2.0']

setup_kwargs = {
    'name': 'chronos-api',
    'version': '0.1.0',
    'description': 'API for my timesheet',
    'long_description': '=======\nchronos\n=======\n\n\n.. image:: https://img.shields.io/pypi/v/chronos.svg\n        :target: https://pypi.python.org/pypi/chronos-api\n\n.. image:: https://img.shields.io/travis/jonaylor89/chronos.svg\n        :target: https://travis-ci.org/jonaylor89/chronos\n\n.. image:: https://ci.appveyor.com/api/projects/status/jonaylor89/branch/master?svg=true\n    :target: https://ci.appveyor.com/project/jonaylor89/chronos/branch/master\n    :alt: Build status on Appveyor\n\n.. image:: https://readthedocs.org/projects/chronos/badge/?version=latest\n        :target: https://chronos.readthedocs.io/en/latest/?badge=latest\n        :alt: Documentation Status\n\n\n.. image:: https://pyup.io/repos/github/jonaylor89/chronos/shield.svg\n     :target: https://pyup.io/repos/github/jonaylor89/chronos/\n     :alt: Updates\n\n\n\nAPI for my timesheet\n\n\n* Free software: MIT license\n\n* Documentation: https://jonaylor89.github.io/chronos\n\n\nExecution\n===========\n\n.. code-block:: console\n\n    $ docker run -e PORT=8000 jonaylor/chronos\n',
    'author': 'John Naylor',
    'author_email': 'jonaylor89@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://jonaylor89.github.io/chronos',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
