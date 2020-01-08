# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['template_magic']

package_data = \
{'': ['*']}

install_requires = \
['ipython>=7.11.1,<8.0.0']

setup_kwargs = {
    'name': 'template-ipython-magic',
    'version': '0.1.0',
    'description': 'IPython magics to render cells as templates in a variety of different templating languages.',
    'long_description': '',
    'author': 'Jez Cope',
    'author_email': 'j.cope@erambler.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/jezcope/template-ipython-magic',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
