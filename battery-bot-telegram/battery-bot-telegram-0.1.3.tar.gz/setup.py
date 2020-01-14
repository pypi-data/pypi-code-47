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
    'version': '0.1.3',
    'description': 'Telegram bot that notifies when battery is low',
    'long_description': '# Telegram battery bot.\n\nMonitors laptop battery level and sends a message on Telegram when it drop below specified threshold.\n\n## Usage:\n\n    batbottg -t TELEGRAM_TOKEN -u TELEGRAM_USER [-b BATTERY_THRESHOLD] [-f CHECK_FREQUENCY]\n    batbottg -c CONFIG_FILE\n    batbottg --help\n\n## Options:\n\n    -t, --telegram-token=TELEGRAM_TOKEN         Telegram bot token\n    -u, --telegram-user=TELEGRAM_USER           Telegram user ID\n    -b, --battery-threshold=BATTERY_THRESHOLD   Battery level alert threshold [default: 10]\n    -f, --check-frequency=CHECK_FREQUENCY       Level check frequency [default: 60]\n    -c, --config=CONFIG_FILE                    Read config from file\n    --help                                      Show this screen\n\n## Config file format:\n\n    [bot]\n    telegram_token = TELEGRAM_TOKEN\n    telegram_user = TELEGRAM_USER\n    battery_threshold = BATTERY_THRESHOLD\n    check_frequency = CHECK_FREQUENCY\n',
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
