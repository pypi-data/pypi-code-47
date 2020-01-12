# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sparkql', 'sparkql.fields']

package_data = \
{'': ['*']}

install_requires = \
['pyspark==2.4.1']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses>=0.7.0,<0.8.0']}

entry_points = \
{'console_scripts': ['lint = tasks:lint',
                     'reformat = tasks:reformat',
                     'test = tasks:test',
                     'typecheck = tasks:typecheck',
                     'verify-all = tasks:verify_all']}

setup_kwargs = {
    'name': 'sparkql',
    'version': '0.1.0',
    'description': 'sparkql: Apache Spark SQL DataFrame schema management for sensible humans',
    'long_description': None,
    'author': 'Matt J Williams',
    'author_email': 'mattjw@mattjw.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mattjw/sparkql',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.8,<4.0.0',
}


setup(**setup_kwargs)
