# -*- coding: utf-8 -*-
from distutils.core import setup

package_dir = \
{'': 'src'}

packages = \
['panaetius']

package_data = \
{'': ['*']}

install_requires = \
['pylite>=0.1.0,<0.2.0', 'toml>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'panaetius',
    'version': '1.0.2',
    'description': 'Python module to gracefully handle a .config file/environment variables for scripts, with built in masking for sensitive options. Provides a Splunk friendly logger instance.',
    'long_description': 'Author\n=======\n\nDaniel Tomlinson (dtomlinson@panaetius.co.uk)\n\nRequires\n=========\n\n`>= python3.7`\n\nPython requirements\n====================\n\n- toml = "^0.10.0"\n- pylite = "^0.1.0"\n\nDocumentation\n==============\n\nRead the documentation on `read the docs`_.\n\n.. _read the docs: https://panaetius.readthedocs.io/en/latest/introduction.html\n\nInstallation\n==============\n\nYou can install ..:obj:`panaetius`\n\nEasy Way\n=========\n\nPython\n-------\n\nFrom pip\n~~~~~~~~~\n\nFrom local wheel\n~~~~~~~~~~~~~~~~~\n\nFrom source\n~~~~~~~~~~~~\n\nExample Usage\n==============\n\n',
    'author': 'dtomlinson',
    'author_email': 'dtomlinson@panaetius.co.uk',
    'url': 'https://github.com/dtomlinson91/panaetius',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
