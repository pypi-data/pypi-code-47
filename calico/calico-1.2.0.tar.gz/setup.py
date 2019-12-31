# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['calico']

package_data = \
{'': ['*']}

install_requires = \
['pexpect>=4.6,<5.0', 'ruamel.yaml>=0.15.41,<0.16.0']

extras_require = \
{':python_version >= "2.7" and python_version < "3.0"': ['enum34>=1.1,<2.0']}

entry_points = \
{'console_scripts': ['calico = calico.cli:main']}

setup_kwargs = {
    'name': 'calico',
    'version': '1.2.0',
    'description': 'I/O checker for command line programs.',
    'long_description': 'Calico is a utility for checking command-line programs in terms of their\ninput and output. It checks whether a program generates the correct output\nwhen given some inputs. It was developed to evaluate simple programming\nassignments in an introductory programming course.\n\nGetting started\n---------------\n\nYou can install Calico using pip::\n\n   pip install calico\n\nCalico uses `pexpect`_ for interacting with the program it is checking.\nThe file that specifies the inputs and outputs for the checks\nis in `YAML`_ format.\n\n.. _pexpect: https://pexpect.readthedocs.io/\n.. _YAML: http://www.yaml.org/\n\nGetting help\n------------\n\nThe online documentation is available on: https://calico.readthedocs.io/\n\nThe source code can be obtained from: https://github.com/itublg/calico\n\nLicense\n-------\n\nCopyright (C) 2016-2019 H. Turgut Uyar <uyar@itu.edu.tr>\n\nSee ``AUTHORS.rst`` for a list of all contributors.\n\nCalico is released under the GPL license, version 3 or later. Read\nthe included ``LICENSE.txt`` for details.\n',
    'author': 'H. Turgut Uyar',
    'author_email': 'uyar@itu.edu.tr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/itublg/calico',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
