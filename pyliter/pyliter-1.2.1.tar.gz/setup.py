# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyliter', 'pyliter.color', 'pyliter.resources']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'pyglet>=1.4.8,<2.0.0', 'pyyaml>=5.2,<6.0']

entry_points = \
{'console_scripts': ['pyliter = pyliter.__main__:pyliter_cli']}

setup_kwargs = {
    'name': 'pyliter',
    'version': '1.2.1',
    'description': 'Generate color syntax highlighted PNG image from python source files.',
    'long_description': 'pyliter - Python syntax highlighting\n====================================\n\n``pyliter`` is a Python 3 command-line tool that generates PNG files\nfrom python source. \n\n\nFeatures\n--------\n\n- syntax highlighting\n- PNG files\n- preview mode\n- OpenGL rendering using pyglet\n\nInstall\n-------\n\n::\n\n   $ pip install pyliter\n\n\n::\n\n   $ pip install git+https://github.com/JnyJny/pyliter\n\n\nUsage\n-----\n\n::\n\n   $ pyliter --help\n\n   Usage: pyliter [OPTIONS] [INPUT_FILE] [OUTPUT_FILE]\n   \n     Python syntax highlighting\n   \n     Performs Python syntax highlighting on code found in INPUT_FILE and writes\n     color annotated text in PNG format to OUTPUT_FILE.\n   \n   Options:\n     -l, --start-line INTEGER  line to begin displaying\n     -n, --line-count INTEGER  number of lines to display\n     -p, --preview\n     -t, --transparent\n     -s, --style-name TEXT\n     --list-styles\n     --version                 Show the version and exit.\n     --help                    Show this message and exit.\n      \n\n\nExample\n-------\n\n.. image:: https://github.com/JnyJny/pyliter/blob/master/examples/screenshot.png\n\t   :width: 400\n\t   :alt: Super Awesome PNG Screenshot\n\n \n',
    'author': 'jnyjny',
    'author_email': 'erik.oshaughnessy@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/JnyJny/pyliter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
