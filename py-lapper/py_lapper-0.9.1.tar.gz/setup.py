# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_lapper']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py-lapper',
    'version': '0.9.1',
    'description': 'A pure python port of nim-lapper.',
    'long_description': '# py_lapper\n\nA pure python port of nim-lapper. Please also the rust lib, rust-lapper\n\nStay tuned for scailist as well\n\n## Install\n\n```bash\n# Not yet on pypi\n# pip install py_lapper\n```\n\n## Usage\n\n```python\nfrom py_lapper import Interval, Lapper, Cursor\n\nintervals = [Interval(0, 5, True), Interval(4, 8, True), Interval(9, 12,\nTrue)]\n\nlapper = Lapper(intervals)\n\nfor iv in lapper.find(4, 7):\n\tprint(iv)\n\n# Use seek when you will have many queries in sorted order. \ncursor = Cursor(0)\nfor iv in lapper.seek(1, 4, cursor):\n\tprint(iv)\nprint(cursor)\n\nfor iv in lapper.seek(5, 7, cursor):\n\tprint(iv)\nprint(curosr)\n```\n',
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
