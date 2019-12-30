# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['clii']
setup_kwargs = {
    'name': 'clii',
    'version': '0.1.1',
    'description': 'Function annotations -> argparse parser',
    'long_description': '# clii\n\nA dead simple way to generate a CLI (via argparse) using Python 3.7+ function\nannotations.\n\nRight now it\'s nearly featureless, but it does support subcommands! See\n`test_clii.py` for more details.\n\n## Installation\n\n```sh\npython3.7 -m pip install --user clii\n```\n\n## Usage\n\n```python\nfrom clii import App, Arg\n\ncli = App(description=__doc__)\n\n\n@cli.main\ndef say_hello(name: str, \n              greeting: Arg(\'-g\', str, \'Greeting to use\') = \'hello\'):\n    """Sum two numbers."""\n    print(f\'{greeting}, {name}\')\n\n\nif __name__ == \'__main__\':\n    cli.run() \n```\n\ngives you\n\n```sh\n$ ./test_hello.py -h\n\nusage: test_hello.py [-h] [--greeting GREETING] name\n\nGreet somebody.\n\npositional arguments:\n  name\n\n  optional arguments:\n    -h, --help            show this help message and exit\n    --greeting GREETING, -g GREETING\n                            Greeting to use. Default: hello\n```\n',
    'author': "James O'Beirne",
    'author_email': 'james.obeirne@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
