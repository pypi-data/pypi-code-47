# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['config_file', 'config_file.parsers']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=5.2,<6.0', 'toml>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'config-file',
    'version': '0.5.0',
    'description': 'Manage your configuration files.',
    'long_description': '# Config File \n\n> Manage and manipulate your configuration files\n\n[![Python 3.8.0|](https://img.shields.io/badge/python-3.8.0-blue.svg)](https://www.python.org/downloads/release/python-380/) \n[![Version](https://img.shields.io/pypi/v/config-file)](https://pypi.org/project/config-file/)\n[![Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)\n[![Build Status](https://travis-ci.com/eugenetriguba/config_file.svg?branch=master)](https://travis-ci.com/eugenetriguba/config_file)\n[![Codecov](https://codecov.io/gh/eugenetriguba/config_file/graph/badge.svg)](https://codecov.io/gh/eugenetriguba/config_file)\n\n> This python package is currently a work in progress and is in a pre-alpha phase. The API is liable to break until v1.\n\nConfig File allows you to use the same simple API for manipulating INI, JSON, \nYAML, and TOML configuration files. For the time being, it only supports INI.\n\n## Installation\n```bash\n$ pip install config_file\n```\n\n## Example\n\nThe `config_file` package exposes `ConfigFile`, `ParsingError`, and `BaseParser` to the public API.\n\n### Sample Configuration File\n\n`config.ini`\n```ini\n[calendar]\ntoday = monday\nstart_week_on_sunday = false\ntoday_index = 0\nquarter_hours_passed = 0.25\n```\n\n### Create a ConfigFile\n```python\nfrom config_file import ConfigFile\n\nconfig = ConfigFile("~/.config/test/config.ini")\n```\n\n### Output your config file as a string\n```python\nconfig.stringify()\n>>> \'[calendar]\\ntoday = monday\\nstart_week_on_sunday = false\\ntoday_index = 0\\nquarter_hours_passed = 0.25\\n\\n\'\n```\n\n### Retrieve values or sections\nA section.key format is used for retrieving and setting values.\n```python\n# Values from the config file are automatically parsed\nconfig.get("calendar.start_week_on_sunday")\n>>> False\n\n# Unless you don\'t want them to be parsed\nconfig.get("calendar.start_week_on_sunday", parse_type=False)\n>>> \'false\'\n\nconfig.get("calendar")\n>>> {\'today\': \'monday\', \'start_week_on_sunday\': False, \'today_index\': 0, \'quarter_hours_passed\': 0.25}\n```\n\n### Set values\n```python\nconfig.set("calendar.today_index", 20)\n>>> True\nconfig.stringify()\n>>> \'[calendar]\\ntoday = monday\\nstart_week_on_sunday = false\\ntoday_index = 20\\nquarter_hours_passed = 0.25\\n\\n\'\n\n# If you specify a section that isn\'t in your config file, the section and the key are added for you.\nconfig.set("week.tuesday_index", 2)\n>>> True\nconfig.stringify()\n>>> \'[calendar]\\ntoday = monday\\nstart_week_on_sunday = false\\ntoday_index = 20\\nquarter_hours_passed = 0.25\\n\\n[week]\\ntuesday_index = 2\\n\\n\'\n```\n\n### Delete sections or key/value pairs.\n```python\nconfig.delete(\'week\')\n>>> True\nconfig.stringify()\n>>> \'[calendar]\\ntoday = monday\\nstart_week_on_sunday = false\\ntoday_index = 20\\nquarter_hours_passed = 0.25\\n\\n\'\n\nconfig.delete(\'calendar.today\')\n>>> True\nconfig.stringify()\n>>> \'[calendar]\\nstart_week_on_sunday = false\\ntoday_index = 20\\nquarter_hours_passed = 0.25\\n\\n\'\n```\n\n\n### Check whether you have a particular section or key\n```python\nconfig.has(\'calendar\')\n>>> True\n\nconfig.has(\'week\')\n>>> False\n\nconfig.has(\'calendar.start_week_on_sunday\')\n>>> True\n```\n\n### Save when you\'re done\nThe contents are only written back out when you call `save()`.\n```python\nconfig.save()\n>>> True\n```\n\n### Reset the file back to its original \n\nThe current configuration file would be deleted and replaced by a copy of the original. \nBy default, since our passed in config file was at path `~/.config/test/config.ini`, `reset()` \nwill look for `~/.config/test/config.original.ini`.\n\n```python\nconfig.reset()\n>>> True\n\n# But you can also specify the original config file explicitly.\nconfig.reset(original_file_path="~/some_other_directory/this_is_actually_the_original.ini")\n>>> True\n```\n\n## Using your own parser\n\n> This feature is a work in-progress and has not been tested yet.\n\nYou can still use config file, even if you don\'t use one of our supported configuration formats. The `ConfigFile` object swaps in the parser it needs based on the file format. However, the constructor takes in an optional `parser` argument that you can use to supply your own custom parser. The only requirement is that the parser must be a concrete implementation of `BaseParser`. \n',
    'author': 'Eugene Triguba',
    'author_email': 'eugenetriguba@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/eugenetriguba/config_file',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
