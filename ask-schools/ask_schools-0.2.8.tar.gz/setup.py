# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['ask_schools']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ask-schools',
    'version': '0.2.8',
    'description': 'Ask Scholars Portal Name Conversion',
    'long_description': "# Ask Schools\n\n[\n![PyPI](https://img.shields.io/pypi/v/ask_schools.svg)\n![PyPI](https://img.shields.io/pypi/pyversions/ask_schools.svg)\n![PyPI](https://img.shields.io/github/license/guinslym/ask_schools.svg)\n](https://pypi.org/project/ask_schools/)\n[![TravisCI](https://travis-ci.org/guinslym/ask_schools.svg?branch=master)](https://travis-ci.org/guinslym/ask_schools)\n\n\nThis package helps convert Ask School suffixes to the school full name.\n\n\n## Installation\n\n**Ask Schools** can be installed from PyPI using `pip` or your package manager of choice:\n\n```\npip install ask_schools\n```\n\n## Usage\n\n\nExample:\n\n```python\n\nfrom ask_schools import find_school_by_operator_suffix\n\ndef check_school_name_equal_toronto():\n  result = find_school_by_operator_suffix('_tor')\n  assert result == 'Tordonto'\n```\n\n## Code of Conduct\n\nEveryone interacting in the project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [PyPA Code of Conduct](https://www.pypa.io/en/latest/code-of-conduct/).\n",
    'author': 'Guinsly Mondesir',
    'author_email': 'guinslym@gmail.com',
    'url': 'https://github.com/guinslym/flake8-markdown',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
