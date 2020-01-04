# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['async_bgm_api', 'async_bgm_api.models']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.0.0,<4.0.0', 'pydantic>=1.2,<2.0']

extras_require = \
{'docs': ['sphinx>=2.3.1,<3.0.0', 'sphinx_rtd_theme==0.4.3']}

setup_kwargs = {
    'name': 'async-bgm-api',
    'version': '0.0.4',
    'description': '',
    'long_description': None,
    'author': 'Trim21',
    'author_email': 'i@trim21.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
