# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alphanum']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'alphanum',
    'version': '0.2.0',
    'description': 'Generates random alphanumeric strings.',
    'long_description': '# alphanum\n\nSimple Python library to generate pseudo-random alphanumeric strings of\narbitrary length. Requires Python 3.5+.\n\n## Installation\n\nalphanum can be obtained from PyPI with `pip install alphanum`.\n\nAlternatively, build it with [Poetry](https://python-poetry.org/):\n\n```bash\npip install poetry\ngit clone https://github.com/clpo13/alphanum\ncd alphanum\npoetry build\npip install dist/alphanum-x.y.z-py3-none-any.whl\n```\n\n## Usage\n\n```python\nimport alphanum\n\nfoo = alphanum.generate(10)\nprint(foo)\n```\n\n## License\n\nCopyright (c) 2020 Cody Logan. MIT licensed.\n',
    'author': 'Cody Logan',
    'author_email': 'clpo13@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/clpo13/alphanum',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
