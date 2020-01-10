# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fracx', 'fracx.collector', 'fracx.metrics', 'fracx.util']

package_data = \
{'': ['*'], 'fracx': ['api/*']}

install_requires = \
['attr>=0.3.1,<0.4.0',
 'attrdict>=2.0.1,<3.0.0',
 'attrs>=19.3.0,<20.0.0',
 'click>=7.0,<8.0',
 'colorama>=0.4.3,<0.5.0',
 'datadog>=0.33.0,<0.34.0',
 'flask-sqlalchemy>=2.4.1,<3.0.0',
 'json_log_formatter>=0.2.0,<0.3.0',
 'logutils>=0.3.5,<0.4.0',
 'psycopg2-binary>=2.8.4,<3.0.0',
 'pyparsing>=2.4.6,<3.0.0',
 'pyproj>=2.4.2,<3.0.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'python-dotenv>=0.10.3,<0.11.0',
 'pyyaml>=5.2,<6.0',
 'spacy>=2.2.3,<3.0.0',
 'sqlalchemy>=1.3.12,<2.0.0',
 'tomlkit>=0.5.8,<0.6.0',
 'xlrd>=1.2.0,<2.0.0']

entry_points = \
{'console_scripts': ['fracx = fracx.manage:main']}

setup_kwargs = {
    'name': 'fracx',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Brock Friedrich',
    'author_email': 'brocklfriedrich@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
