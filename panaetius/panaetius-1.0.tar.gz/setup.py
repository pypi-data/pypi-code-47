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
    'version': '1.0',
    'description': 'Python module to gracefully handle a .config file/environment variables for scripts, with built in masking for sensitive options. Provides a Splunk friendly logger instance.',
    'long_description': '# Author\n\nDaniel Tomlinson (dtomlinson@panaetius.co.uk)\n\n# Requires\n\n`>= python3.7`\n\n# Python requirements\n\n- toml = "^0.10.0"\n- pylite = "^0.1.0"\n\n# Documentation\n\n_soon_\n\n# Installation\n\n_soon_\n\n# Easy Way\n\n## Python\n\n### From pip\n\n### From local wheel\n\n### From source\n\n# Example Usage\n\n',
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
