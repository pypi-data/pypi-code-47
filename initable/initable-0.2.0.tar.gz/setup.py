# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['initable', 'initable._vendor']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'initable',
    'version': '0.2.0',
    'description': 'Initable is a Python package that helps create DRY-er classes.',
    'long_description': '<div align="center">\n  <h1>Initable</h1>\n  <a href=https://github.com/paysonwallach/initable/releases/latest>\n    <img src=https://img.shields.io/github/v/release/paysonwallach/initable?style=flat-square>\n  </a>\n  <a href=https://github.com/paysonwallach/initable/blob/master/LICENSE>\n    <img src=https://img.shields.io/badge/license-HIP-994444?style=flat-square>\n  </a>\n  <a href=https://buymeacoffee.com/paysonwallach>\n    <img src=https://img.shields.io/badge/donate-Buy%20me%20a%20coffee-yellow?style=flat-square>\n  </a>\n  <br>\n  <br>\n  <br>\n</div>\n\n[Initable](https://github.com/paysonwallach/initable) is a Python package that helps create [DRY](https://en.wikipedia.org/wiki/Don\'t_repeat_yourself)-er classes.\n\n## Installation\n\n[Initable](https://github.com/paysonwallach/initable) is available through [pip](https://pypi.org/project/initable/).\n\n```bash\npip install initable\n```\n\n## Usage\n\nDefine an instance method you would like to be able to initialize the class with as well.\n\n```python\nfrom initable import initializable\n\nclass Foo(object):\n    @initializable\n    def bar(self, arg):\n        self.baz = do_something(arg)\n```\n\nYou can now call that method on the class and receive an initialized instance upon completion:\n\n```python\nfoo = Foo.bar(arg)\n```\n\nOr call the method on an existing instance:\n\n```python\nfoo = Foo()\n# do stuff...\nfoo.bar(arg)  # `bar()` is called on instance `foo`\n```\n\n## Testing\n\nRun the following from the root of the project:\n\n```bash\npoetry run pytest tests/\n```\n\n## Contributing\n\nPull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## Code of Conduct\n\nBy participating in this project, you agree to abide by the terms of the [Code of Conduct](https://github.com/paysonwallach/initable/blob/master/CODE_OF_CONDUCT.md).\n\n## License\n[Initable](https://github.com/paysonwallach/initable) is licensed under the [Hippocratic License](https://github.com/paysonwallach/initable/blob/master/LICENSE).\n',
    'author': 'Payson Wallach',
    'author_email': 'paysonwallach@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
