# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['latextomd']

package_data = \
{'': ['*']}

install_requires = \
['TexSoup>=0.2.0,<0.3.0']

entry_points = \
{'console_scripts': ['latextomd = latextomd.cli:main']}

setup_kwargs = {
    'name': 'latextomd',
    'version': '0.1.1',
    'description': 'Simple project to convert latex in markdown',
    'long_description': '# latextomd\n\nA simple python package to convert latex to markdown (katex)\n\n## Installation\n\n```bash\npip install latextomd\n```\n\n## Basic usage\n\n```bash\nlatextomd source.tex export.md\n```\n\n',
    'author': 'David Couronné',
    'author_email': 'couronne.david@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DavidCouronne/latextomd',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
