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
    'version': '0.4.0',
    'description': 'Manage your configuration files.',
    'long_description': '# Config File \n\n> Manage and manipulate your configuration files\n\n[![Python 3.8.0|](https://img.shields.io/badge/python-3.8.0-blue.svg)](https://www.python.org/downloads/release/python-380/) \n[![Version](https://img.shields.io/pypi/v/config-file)](https://pypi.org/project/config-file/)\n[![Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)\n[![Build Status](https://travis-ci.com/eugenetriguba/config_file.svg?branch=master)](https://travis-ci.com/eugenetriguba/config_file)\n\n> This python package is currently a work in progress and is in a pre-alpha phase. The API is liable to break until v1.\n\nConfig File allows you to use the same simple API for manipulating INI, JSON, \nYAML, and TOML configuration files. For the time being, it only supports INI.\n\n## Installation\n```bash\n$ pip install config_file\n```\n\n## Examples\n\n`config.ini`\n```ini\n[calendar]\ntoday = monday\nstart_week_on_sunday = false\ntoday_index = 0\nquarter_hours_passed = 0.25\n```\n\n`example.py`\n```python\nfrom config_file import ConfigFile\n\nconfig = ConfigFile("~/.config/test/config.ini")\n\n# Output your config file as a string\nconfig.stringify()\n>>> \'[calendar]\\ntoday = monday\\nstart_week_on_sunday = false\\ntoday_index = 0\\nquarter_hours_passed = 0.25\\n\\n\'\n\n# Retrieve values with a section.key format\nconfig.get("calendar.today")\n>>> \'monday\'\n\n# Values from the config file are automatically parsed\nconfig.get("calendar.start_week_on_sunday")\n>>> False\n\n# Values from the config file are automatically parsed\nconfig.get("calendar.start_week_on_sunday")\n>>> False\n\n# Unless you don\'t want them to be parsed\nconfig.get("calendar.today_index", parse_type=False)\n>>> \'0\'\n\n# The dot syntax is also used to set values. True is returned on success.\nconfig.set("calendar.today_index", 20)\n>>> True\nconfig.stringify()\n>>> \'[calendar]\\ntoday = monday\\nstart_week_on_sunday = false\\ntoday_index = 20\\nquarter_hours_passed = 0.25\\n\\n\'\n\n# If you specify a section that isn\'t in your config file, the section and the key are added for you.\nconfig.set("week.tuesday_index", 2)\n>>> True\nconfig.stringify()\n>>> \'[calendar]\\ntoday = monday\\nstart_week_on_sunday = false\\ntoday_index = 20\\nquarter_hours_passed = 0.25\\n\\n[week]\\ntuesday_index = 2\\n\\n\'\n\n# Delete can delete an entire section or just a key/value pair.\nconfig.delete(\'week\')\n>>> True\nconfig.stringify()\n>>> \'[calendar]\\ntoday = monday\\nstart_week_on_sunday = false\\ntoday_index = 20\\nquarter_hours_passed = 0.25\\n\\n\'\n\n# Delete can delete an entire section or just a key/value pair.\nconfig.delete(\'calendar.today\')\n>>> True\nconfig.stringify()\n>>> \'[calendar]\\nstart_week_on_sunday = false\\ntoday_index = 20\\nquarter_hours_passed = 0.25\\n\\n\'\n\n# You can also just check if the file has a particular section or key.\nconfig.has(\'calendar\')\n>>> True\nconfig.has(\'week\')\n>>> False\nconfig.has(\'calendar.start_week_on_sunday\')\n>>> True\n\n# The file is only written back out when you call save()\nconfig.save()\n>>> True\n\n# You can also reset the file back to its original state. The current configuration file \n# would be deleted and replaced by a copy of the original. By default, since our passed in\n# config file was at path `~/.config/test/config.ini`, `reset()` will look for \n# `~/.config/test/config.original.ini`\nconfig.reset()\n>>> True\n\n# Or you can specify the file path explicitly\nconfig.reset(original_file_path="~/some_other_directory/this_is_actually_the_original.ini")\n>>> True\n```\n',
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
