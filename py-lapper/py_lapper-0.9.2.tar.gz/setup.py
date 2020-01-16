# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_lapper']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py-lapper',
    'version': '0.9.2',
    'description': 'A pure python port of nim-lapper.',
    'long_description': '# py_lapper\n[![PyPI version](https://badge.fury.io/py/py-lapper.svg)](https://badge.fury.io/py/py-lapper)\n![Coverage](./coverage.svg)\n\n\nA pure python port of [nim-lapper](https://github.com/brentp/nim-lapper). Please also see the rust lib, [rust-lapper](https://crates.io/crates/rust-lapper)\n\nStay tuned for a pyO3 wrapper for the rust lib.\n\n## Install\n\n```bash\npip install py_lapper\n```\n\n## Usage\n\n```python\nfrom py_lapper import Interval, Lapper, Cursor\n\nintervals = [Interval(0, 5, True), Interval(4, 8, True), Interval(9, 12, True)]\nlapper = Lapper(intervals)\n\nfound = [iv for iv in lapper.find(4, 7)]\n# found = [Interval(0, 5, True), Interval(4, 8, True)]\n\n# Use seek when you will have many queries in sorted order.\ncursor = Cursor(0)\nfound = [iv for iv in lapper.seek(1, 4, cursor)]\n# found = [Interval(0, 5, True)]\n# cursor = Cursor(2)\n\nfound = [iv for iv in lapper.seek(5, 7, cursor)]\n# found = [Interval(4, 8, True)]\n# cursor = Cursor(3)\n```\n',
    'author': 'Seth Stadick',
    'author_email': 'sstadick@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sstadick/py-lapper',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
