# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flake8_click']

package_data = \
{'': ['*']}

install_requires = \
['attrs', 'click>=7.0,<8.0', 'flake8>=3.7,<4.0', 'libcst>=0.2.4,<0.3.0']

entry_points = \
{'flake8.extension': ['r2c-click-best-practices = '
                      'flake8_click.flake8_click:ClickPracticeCheckers']}

setup_kwargs = {
    'name': 'flake8-click',
    'version': '0.3.0',
    'description': 'Checks for click, by r2c. Available in [Bento](https://bento.dev).',
    'long_description': "# click-linter\n\nFlake8 plugin for detecting click best practices\n\n## Checks\n\n- `r2c-click-option-function-argument-check`: missing argument for `click.option`\n- `r2c-click-names-are-well-formed`: checks for\n  - click option name does not begin with '-'\n  - click argument name begins with '-'\n  - click parameter is missing name\n- `r2c-click-launch-uses-literal`: `click.launch` may be called with user input, leading to a security\n  vulnerability\n\n## Installing\n\n```\n$ python -m pip install flake8-click\n```\n\n_Specify `python2` or `python3` to install for a specific Python version._\n\nAnd double check that it was installed correctly:\n\n```\n$ python -m flake8 -h\nUsage: flake8 [options] file file ...\n\n...\n\nInstalled plugins: flake8-click : 0.1.0, mccabe: 0.5.3, pycodestyle: 2.2.0, pyflakes: 1.3.0\n```\n\nNote the `flake8-click: 0.1.0`.\n\n## Using\n\nClick best practices is a flake8 plugin. You can easily use this plugin by\n\n```\n$ python -m flake8 --select=CLC /path/to/code\n```\n\n## Testing\n\n```\n$ pytest\n```\n",
    'author': 'R2C',
    'author_email': 'hello@returntocorp.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://bento.dev',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
