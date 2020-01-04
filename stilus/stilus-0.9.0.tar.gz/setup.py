# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stilus', 'stilus.functions', 'stilus.nodes', 'stilus.stack', 'stilus.visitor']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4',
 'click',
 'deprecated',
 'lxml',
 'pillow',
 'pyyaml',
 'setuptools>=44.0.0,<45.0.0',
 'watchdog>=0.8.3,<0.9.0',
 'wheel']

entry_points = \
{'console_scripts': ['stilus = stilus.cli:stilus']}

setup_kwargs = {
    'name': 'stilus',
    'version': '0.9.0',
    'description': 'A Stylus css compiler in Python.',
    'long_description': '\n# Stilus\n\n[![Travis (.org) branch](https://img.shields.io/travis/jw/stilus/master.svg?style=flat-square)](https://travis-ci.org/jw/stilus)\n[![Codecov branch](https://img.shields.io/codecov/c/github/jw/stilus/master.svg?style=flat-square)](https://codecov.io/gh/jw/stilus)\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/stilus.svg?style=flat-square)](https://pypi.org/project/stilus/#files)\n[![PyPI](https://img.shields.io/pypi/v/stilus.svg?style=flat-square)](https://pypi.org/project/stilus/#history)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/stilus.svg?style=flat-square)](https://pypi.org/project/stilus/#description)\n[![PyPI - License](https://img.shields.io/pypi/l/stilus?style=flat-square)](https://pypi.org/project/stilus/)\n\nA Stylus css compiler in Python.\n\n## Installation\n\nInstall and update using [pip](https://pypi.org/project/pip/):\n\n    $ python -m pip install -U stilus\n\nor \n\n    $ pip install -U stilus\n\n## Documentation\n\nThere is [some documentation](https://stilus.readthedocs.io) available.\n\n## Missing\n\nSome parts of Stylus are not in Stilus yet:\n\n - Caching\n - Plugins\n - Documentation\n\nAll help is appreciated!\n',
    'author': 'Jan Willems',
    'author_email': 'jw@elevenbits.com',
    'maintainer': 'Jan Willems',
    'maintainer_email': 'jw@elevenbits.com',
    'url': 'https://github.com/jw/stilus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
