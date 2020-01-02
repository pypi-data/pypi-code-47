# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pybtex_author_year_label']

package_data = \
{'': ['*']}

install_requires = \
['pelican>=4.2,<5.0', 'pybtex>=0.22.2,<0.23.0', 'pytest-mock>=1.13.0,<2.0.0']

entry_points = \
{'pybtex.style.labels': ['author_year_1 = pybtex_author_year_label:LabelStyle1',
                         'author_year_2 = '
                         'pybtex_author_year_label:LabelStyle2']}

setup_kwargs = {
    'name': 'pybtex-author-year-label',
    'version': '1.0.0',
    'description': 'Defines an author-year inline citation style for Pybtex.',
    'long_description': '# Author-year labels for Pybtex\n\nDefines an author-year inline citation style for [Pybtex](https://pybtex.org/). This is\nmodified from the alpha style built into Pybtex, written by\nAndrey Golovizin.\n\n## Available styles\n\nThis plugin defines two styles:\n\n### `author_year_1`\n\nThis style will format the label like `(Einstein,1911)`\n\n### `author_year_2`\n\nThis style will format the label like `Einstein (1911)`\n',
    'author': 'Johan Vergeer',
    'author_email': 'johanvergeer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/johanvergeer/pybtex-author-year-label',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
