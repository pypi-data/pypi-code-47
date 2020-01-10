# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['betterconf']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'betterconf',
    'version': '1.5',
    'description': 'Minimalistic Python library for your configs.',
    'long_description': '# Minimalistic Python library for your configs.\n\n## How to?\nAt first, install libary:\n\n```sh\npip install betterconf\n```\n\nAnd... write simple config:\n```python\nfrom betterconf import field, Config\n\nclass MyConfig(Config):\n    my_var = field("my_var")\n\ncfg = MyConfig()\nprint(cfg.my_var)\n```\n\nTry to run:\n```sh\nmy_var=1 python our_file.py\n```\n\nWith default values:\n```python\nfrom betterconf import field, Config\n\nclass MyConfig(Config):\n    my_var = field("my_var", default="hello world")\n\ncfg = MyConfig()\nprint(cfg.my_var)\n# hello world\n```\n\nOverride values when it\'s needed (for an example: test cases)\n```python\nfrom betterconf import field, Config\n\nclass MyConfig(Config):\n    my_var = field("my_var", default="hello world")\n\ncfg = MyConfig(my_var="WOW!")\nprint(cfg.my_var)\n# WOW!\n```\n\nBy default `betterconf` gets all values from `os.environ` but sometimes we need much.\nYou can create own `field value provider` in minutes:\n\n```python\nfrom betterconf import field, Config\nfrom betterconf.config import AbstractProvider\n\nclass NameProvider(AbstractProvider):\n    def get(self, name: str):\n        return name\n\nclass Cfg(Config):\n    my_var = field("my_var", provider=NameProvider())\n\ncfg = Cfg()\nprint(cfg.my_var)\n# my_var\n```\n',
    'author': 'prostomarkeloff',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/prostomarkeloff/betterconf',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.1,<4.0',
}


setup(**setup_kwargs)
