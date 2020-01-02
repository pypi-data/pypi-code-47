# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coveragespace', 'coveragespace.tests']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.3,<0.4',
 'coverage',
 'docopt>=0.6,<0.7',
 'minilog',
 'requests>=2.0,<3.0']

entry_points = \
{'console_scripts': ['coveragespace = coveragespace.cli:main']}

setup_kwargs = {
    'name': 'coveragespace',
    'version': '3.0.1',
    'description': 'A place to track your code coverage metrics.',
    'long_description': '# Overview\n\nThe official command-line client for [The Coverage Space](http://coverage.space).\n\n[![Unix Build Status](https://img.shields.io/travis/jacebrowning/coverage-space-cli/master.svg?label=unix)](https://travis-ci.org/jacebrowning/coverage-space-cli)\n[![Windows Build Status](https://img.shields.io/appveyor/ci/jacebrowning/coverage-space-cli/master.svg?label=window)](https://ci.appveyor.com/project/jacebrowning/coverage-space-cli)\n[![Coverage Status](https://img.shields.io/coveralls/jacebrowning/coverage-space-cli/master.svg)](https://coveralls.io/r/jacebrowning/coverage-space-cli)\n[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/jacebrowning/coverage-space-cli.svg)](https://scrutinizer-ci.com/g/jacebrowning/coverage-space-cli/?branch=master)\n[![PyPI Version](https://img.shields.io/pypi/v/coveragespace.svg)](https://pypi.org/project/coveragespace)\n[![PyPI License](https://img.shields.io/pypi/l/coveragespace.svg)](https://pypi.org/project/coveragespace)\n\n# Setup\n\n## Requirements\n\n* Python 3.5+\n\n## Installation\n\nInstall this library directly into an activated virtual environment:\n\n```text\n$ pip install coveragespace\n```\n\nor add it to your [Poetry](https://poetry.eustace.io/) project:\n\n```text\n$ poetry add coveragespace\n```\n\n# Usage\n\nTo update the value for a test coverage metric:\n\n```sh\n$ coveragespace <owner/repo> <metric>\n```\n\nFor example, after testing with code coverage enabled:\n\n```sh\n$ coveragespace owner/repo unit\n```\n\nwill attempt to extract the current coverage data from your working tree and compare that with the last known value. The coverage value can also be manually specified:\n\n```sh\n$ coveragespace <owner/repo> <metric> <value>\n```\n',
    'author': 'Jace Browning',
    'author_email': 'jacebrowning@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://coverage.space/client/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
