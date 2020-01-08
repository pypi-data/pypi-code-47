# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blib2to3', 'blib2to3.pgen2']

package_data = \
{'': ['*']}

modules = \
['lavender']
install_requires = \
['appdirs>=1.4.0,<2.0.0',
 'attrs>=18.1.0,<19.0.0',
 'click>=6.5,<7.0',
 'pathspec>=0.6.0,<0.7.0',
 'regex>=2019.8.19',
 'toml>=0.9.4,<0.10.0',
 'typed-ast>=1.4.0,<2.0.0']

extras_require = \
{'d': ['aiohttp>=3.3.2,<4.0.0', 'aiohttp_cors>=0.7.0,<0.8.0']}

entry_points = \
{'console_scripts': ['lavender = lavender:main']}

setup_kwargs = {
    'name': 'lavender',
    'version': '0.1.1',
    'description': 'The slightly more compromising code formatter.',
    'long_description': '# Lavender\n\n[![PyPI](https://img.shields.io/pypi/v/lavender.svg)](https://pypi.python.org/pypi/lavender)\n\nA slightly more compromising Python code formatter, based on the latest stable release of\n[Black](https://github.com/python/black) (`19.10b0` at the time of writing).\n\n## Differences from Black\n\n- The default line length is 99 instead of 88 (configurable with `--line-length`).\n- Single quoted strings are preferred (configurable with\n `--string-normalization none/single/double`).\n- Empty lines between `class`es and `def`s are treated no differently from other code. The old\n  behavior, which sometimes inserts double empty lines between them, remains available via\n  `--special-case-def-empty-lines`.\n- The Vim plugin configuration variable for line length is named `g:lavender_line_length` instead\n  of `g:lavender_linelength`, for consistency with the other configuration variable names.\n\n## Documentation\n\nRead up on [Black](https://github.com/python/black), but replace `black` with `lavender` in your\nhead.\n\n## License\n\nLavender is Copyright (c) 2019-2020 Michael Smith &lt;michael@spinda.net&gt;\n\nBlack, the software on which it was based, is Copyright (c) 2018 Łukasz Langa\n\nThis program is free software: you can redistribute it and/or modify it under the terms of the MIT\nLicense.\n\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without\neven the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the MIT\nLicense for more details.\n\nYou should have received a [copy](LICENSE) of the MIT License along with this program. If not, see\n[http://opensource.org/licenses/MIT](http://opensource.org/licenses/MIT).\n\n### Contribution\n\nUnless you explicitly state otherwise, any contribution intentionally submitted for inclusion in\nthis work by you shall be licensed as above, without any additional terms or conditions.\n',
    'author': 'Michael Smith',
    'author_email': 'michael@spinda.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/spinda/lavender',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
