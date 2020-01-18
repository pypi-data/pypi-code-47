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
    'version': '0.3.3',
    'description': 'Manage your configuration files.',
    'long_description': '# Config File \n\n> Manage and manipulate your configuration files\n\n[![Python 3.8.0|](https://img.shields.io/badge/python-3.8.0-blue.svg)](https://www.python.org/downloads/release/python-380/) \n[![Version](https://img.shields.io/pypi/v/config-file)](https://pypi.org/project/config-file/)\n[![Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)\n\n> This python package is currently a work in progress and is in a pre-alpha phase. The API is liable to break until v1.\n\nConfig File allows you to use the same simple API for manipulating INI, JSON, \nYAML, and TOML configuration files. For the time being, it only supports INI.\n\n## Motivation\n\nWith applications I was building, I found myself frequently having to use some sort of configuration folder with an object that modeled the configuration file. I did this to help more easily manipulate my configuration. However, I found myself needing this sort of thing for several different applications and would end up rewriting something similar. So ended up deciding to create a package out of it so I could focus more on the application I was building instead.\n\n## Why not just use configparser, ConfigObj, etc.?\n\nI wanted something a bit cleaner and simpler to use than configparser. The ini parser uses configparser under the hood, but it provides some niceties such as automatically parsing configuration values into their native types when you retrieve them. However, I also wanted something more flexible, and ini files aren\'t the only common configuration format. That is why Config File uses an adapter pattern to swap in and out the right parser for various file types you give it. This allows you to use the same API for all of your configuration needs. \n\n## Installation\n```bash\n$ pip install config_file\n```\n\n## Examples\n\n`config.ini`\n```ini\n[calendar]\ntoday = monday\nstart_week_on_sunday = false\ntoday_index = 0\nquarter_hours_passed = 0.25\n```\n\n`example.py`\n```python\nfrom config_file import ConfigFile\n\nconfig = ConfigFile("~/.config/test/config.ini")\n\n# Output your config file as a string\nconfig.stringify()\n>>> \'[calendar]\\ntoday = monday\\nstart_week_on_sunday = false\\ntoday_index = 0\\nquarter_hours_passed = 0.25\\n\\n\'\n\n# Retrieve values with a section.key format\nconfig.get("calendar.today")\n>>> \'monday\'\n\n# Values from the config file are automatically parsed\nconfig.get("calendar.start_week_on_sunday")\n>>> False\n\n# Values from the config file are automatically parsed\nconfig.get("calendar.start_week_on_sunday")\n>>> False\n\n# Unless you don\'t want them to be parsed\nconfig.get("calendar.today_index", parse_type=False)\n>>> \'0\'\n\n# The dot syntax is also used to set values. True is returned on success.\nconfig.set("calendar.today_index", 20)\n>>> True\nconfig.stringify()\n>>> \'[calendar]\\ntoday = monday\\nstart_week_on_sunday = false\\ntoday_index = 20\\nquarter_hours_passed = 0.25\\n\\n\'\n\n# If you specify a section that isn\'t in your config file, the section and the key are added for you.\nconfig.set("week.tuesday_index", 2)\n>>> True\nconfig.stringify()\n>>> \'[calendar]\\ntoday = monday\\nstart_week_on_sunday = false\\ntoday_index = 20\\nquarter_hours_passed = 0.25\\n\\n[week]\\ntuesday_index = 2\\n\\n\'\n\n# Delete can delete an entire section or just a key/value pair.\nconfig.delete(\'week\')\n>>> True\nconfig.stringify()\n>>> \'[calendar]\\ntoday = monday\\nstart_week_on_sunday = false\\ntoday_index = 20\\nquarter_hours_passed = 0.25\\n\\n\'\n\n# Delete can delete an entire section or just a key/value pair.\nconfig.delete(\'calendar.today\')\n>>> True\nconfig.stringify()\n>>> \'[calendar]\\nstart_week_on_sunday = false\\ntoday_index = 20\\nquarter_hours_passed = 0.25\\n\\n\'\n\n# You can also just check if the file has a particular section or key.\nconfig.has(\'calendar\')\n>>> True\nconfig.has(\'week\')\n>>> False\nconfig.has(\'calendar.start_week_on_sunday\')\n>>> True\n```\n',
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
