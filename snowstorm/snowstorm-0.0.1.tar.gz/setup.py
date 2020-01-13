# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snowstorm',
 'snowstorm.request',
 'snowstorm.request.core',
 'snowstorm.request.helpers',
 'snowstorm.resource',
 'snowstorm.resource.fields',
 'snowstorm.resource.query',
 'snowstorm.response']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0',
 'marshmallow>=3.2.2,<4.0.0',
 'pytz>=2019.3,<2020.0',
 'ujson>=1.35,<2.0']

setup_kwargs = {
    'name': 'snowstorm',
    'version': '0.0.1',
    'description': 'ServiceNow library and UI',
    'long_description': '# snowstorm\nServiceNow library and UI\n\nKey characteristics:\n- Async capable\n- Python36+ support\n- Built-in ORM\n- Request parallelism\n- Stream generator\n- Extensible\n- Cross platform UI\n- Permissively licensed\n\n',
    'author': 'Robert Wikman',
    'author_email': 'rbw@vault13.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rbw/snowstorm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
