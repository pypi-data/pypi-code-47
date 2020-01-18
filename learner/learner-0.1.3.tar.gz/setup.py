# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['learner', 'learner.models', 'learner.wrappers']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.1.2,<4.0.0',
 'numpy>=1.17.4,<2.0.0',
 'pandas>=0.25.3,<0.26.0',
 'psutil>=5.6.7,<6.0.0',
 'scikit-learn>=0.22,<0.23',
 'scipy>=1.4.0,<2.0.0',
 'torch>=1.3.0,<2.0.0',
 'torchvision>=0.4.2,<0.5.0',
 'utify>=0.2.0,<0.3.0']

extras_require = \
{'doc': ['sphinx>=2.3.0,<3.0.0',
         'nbsphinx>=0.5.0,<0.6.0',
         'recommonmark>=0.6.0,<0.7.0',
         'sphinx_rtd_theme>=0.4.3,<0.5.0']}

setup_kwargs = {
    'name': 'learner',
    'version': '0.1.3',
    'description': 'One learner to learn the world',
    'long_description': '# learner: One learner to learn the world\n\n[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-375/)\n\nTODO\n',
    'author': 'yajiez',
    'author_email': 'yajiez.me@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/yajiez/learner',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
