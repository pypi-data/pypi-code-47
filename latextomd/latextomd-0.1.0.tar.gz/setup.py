# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['latextomd']

package_data = \
{'': ['*']}

install_requires = \
['TexSoup>=0.2.0,<0.3.0']

setup_kwargs = {
    'name': 'latextomd',
    'version': '0.1.0',
    'description': 'Simple project to convert latex in markdown',
    'long_description': '# latextomd\n\nA simple python package to convert latex to markdown (katex)\n\n',
    'author': 'David Couronné',
    'author_email': 'couronne.david@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DavidCouronne/latextomd',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
