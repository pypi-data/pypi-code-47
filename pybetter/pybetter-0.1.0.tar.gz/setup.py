# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pybetter', 'pybetter.transformers']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'libcst>=0.2.6,<0.3.0']

entry_points = \
{'console_scripts': ['pybetter = pybetter.cli:main']}

setup_kwargs = {
    'name': 'pybetter',
    'version': '0.1.0',
    'description': 'Tool for fixing trivial problems with your code.',
    'long_description': '# pybetter\n![PyPI](https://img.shields.io/pypi/v/pybetter) \n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pybetter)\n![GitHub](https://img.shields.io/github/license/lensvol/pybetter)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nTool for fixing trivial problems with your code.\n\nOriginally intended as an example for my PyCon Belarus 2020 talk about [LibCST](https://github.com/Instagram/LibCST).\n\n## Usage\n\nSimply provide a valid Python source code file as one of the argument and it will try to fix any issues it could find.\n\n```\nUsage: pybetter [OPTIONS] [SOURCES]...\n\nOptions:\n  --noop  Do not make any changes to the source files.\n  --help  Show this message and exit.\n```\n\n\n\n## Example\n\n```shell\n# cat test.py\ndef f():\n  return (42, "Hello, world")\n\n# pybetter test.py\n--> Processing \'test.py\'...\n  [+] (B003) Remove parentheses from the tuple in \'return\' statement.\nAll done!\n\n# cat test.py\ndef f():\n  return 42, "Hello, world"\n\n```\n\n\n\n## Available fixers\n\n* **B001: Replace \'not A in B\' with \'A not in B\'**\n\n  Usage of `A not in B` over `not A in B` is recommended both by Google and [PEP-8](https://www.python.org/dev/peps/pep-0008/#programming-recommendations). Both of those forms are compiled to the same bytecode, but second form has some potential of confusion for the reader. \n\n  ```python\n  # BEFORE:\n  if not 42 in counts:\n    sys.exit(-1)\n  \n  # AFTER:\n  if 42 not in counts:\n    sys.exit(-1)\n  ```\n\n  \n\n* **B002: Default values for `kwargs` are mutable.**\n\n  As described in [Common Gotchas] (https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments) section of "The Hitchhiker\'s Guide to Python", mutable arguments can be a tricky thing. \n\n  This fixer replaces any default values that happen to be lists or dicts with **None** value, moving initialization from function definition into function body.\n\n  ```python\n  # BEFORE\n  def p(a=[]):\n    print(a)\n    \n  # AFTER\n  def p(a=None):\n    if a is None:\n      a = []\n      \n    print(a)\n  ```\n\n  Be warned, that this fix may break code which *intentionally* uses mutable default arguments (e.g. caching).\n\n* **B003: Remove parentheses from the tuple in \'return\' statement.**\n\n  If you are returning a tuple from the function by implicitly constructing it, then additional parentheses around it are redundant.\n\n  ```python\n  # BEFORE:\n  def hello():\n    return ("World", 42)\n  \n  # AFTER:\n  def hello():\n    return "World", 42\n  ```\n\n  \n\n## Installation\n\n```shell script\n# pip install pybetter\n```\n\n## Getting started with development\n\n```shell script\n# git clone https://github.com/lensvol/pybetter\n# poetry install\n```\n\n## License\n\nThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details\n\n## Authors\n\n* **Kirill Borisov** ([lensvol@gmail.com](mailto:lensvol@gmail.com))\n',
    'author': 'Kirill Borisov',
    'author_email': 'lensvol@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lensvol/pybetter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
