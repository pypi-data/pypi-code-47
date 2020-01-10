# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tritise']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'sqlalchemy>=1.3.12,<2.0.0']

entry_points = \
{'console_scripts': ['tritise = tritise.cli:cli']}

setup_kwargs = {
    'name': 'tritise',
    'version': '0.1.1',
    'description': 'A small python library to handle trivial time series in an SQLite database.',
    'long_description': "# tritise\n\nA small python library to handle trivial time series in an SQLite database.\n\n## Installation\n\n`pip install tritise`\n\n## Example\n\n```python\nfrom tritise import Tritise\nt = Tritise('test.sqlite')\nt.add(1.1)\nt.add(2)\nt.add(3.0)\nprint(t.all())\nprint(t.last().value)\n\nfrom dateutil.parser import parse\nt.add(-1, tag='historic', timestamp=parse('1.1.2000'))\nt.add(5, tag='historic', timestamp=parse('15.3.2001'))\nt.add(200, tag='historic', timestamp=parse('21.9.2002'))\n\nt.all('historic')\nt.range(start_date = parse('1.1.2001'), end_date = parse('31.12.2001'), tag = 'historic')\n```\n\n## Command line tool\n\nTritise ships a command line tool (`tritise`) to inspect the created databases.\n\nRun `tritise --help` for more information.\n\n### CLI Example\n\n`tritise dump -d test.sqlite`\n\n",
    'author': 'asmw',
    'author_email': 'asmw@asmw.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/asmw/tritise',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
