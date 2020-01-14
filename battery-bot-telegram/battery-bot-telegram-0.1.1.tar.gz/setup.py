# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['battery_bot_telegram']

package_data = \
{'': ['*']}

install_requires = \
['docopt>=0.6.2,<0.7.0', 'psutil>=5.6,<6.0', 'python-telegram-bot>=12.2,<13.0']

entry_points = \
{'console_scripts': ['batbottg = battery_bot_telegram:run_bot']}

setup_kwargs = {
    'name': 'battery-bot-telegram',
    'version': '0.1.1',
    'description': 'Telegram bot that notifies when battery is low',
    'long_description': None,
    'author': 'Tomasz Walotek',
    'author_email': 'tomasz.walotek@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
