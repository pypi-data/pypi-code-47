# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alphanum']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'alphanum',
    'version': '0.1.1',
    'description': 'Generates random alphanumeric strings.',
    'long_description': '# alphanum\n\nSimple Python library to generate pseudo-random alphanumeric strings of\narbitrary length. Requires Python 3.6+.\n\n## Usage\n\n```python\nimport alphanum\n\nfoo = alphanum.generate(10)\nprint(foo)\n```\n\n## License\n\nCopyright (c) 2020 Cody Logan. MIT licensed.\n',
    'author': 'Cody Logan',
    'author_email': 'clpo13@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/clpo13/alphanum',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
