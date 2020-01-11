# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zuora_aqua_client_cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'flake8>=3.7,<4.0', 'requests>=2.22,<3.0']

entry_points = \
{'console_scripts': ['zacc = zuora_aqua_client_cli.run_zoql:main']}

setup_kwargs = {
    'name': 'zuora-aqua-client-cli',
    'version': '0.1.13',
    'description': 'Run ZOQL queries through AQuA from the command line',
    'long_description': '# zuora-aqua-client-cli [![Build Status](https://travis-ci.com/molnarjani/zuora-aqua-client-cli.svg?branch=master)](https://travis-ci.com/molnarjani/zuora-aqua-client-cli)\n\nRun ZOQL queries through AQuA from the command line\n\n# Usage\n\n#### Zacc\n```\nUsage: zacc [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  bearer    Prints bearer than exits\n  describe  List available fields of Zuora resource\n  query     Run ZOQL Query\n```\n\n#### Query\n```\nUsage: zacc query [OPTIONS]\n\n  Run ZOQL Query\n\nOptions:\n  -c, --config-filename PATH      Config file containing Zuora ouath\n                                  credentials  [default: zuora_oauth.ini]\n  -z, --zoql PATH                 ZOQL file to be executed  [default:\n                                  input.zoql]\n  -o, --output PATH               Where to write the output to, default is\n                                  STDOUT\n  -e, --environment [prod|preprod|local]\n                                  Zuora environment to execute on  [default:\n                                  local]\n  -m, --max-retries INTEGER       Maximum retries for query\n  --help                          Show this message and exit.\n```\n\n#### Describe\n```\nUsage: zacc describe [OPTIONS] RESOURCE\n\n  List available fields of Zuora resource\n\nOptions:\n  -c, --config-filename PATH      Config file containing Zuora ouath\n                                  credentials  [default: zuora_oauth.ini]\n  -e, --environment [prod|preprod|local]\n                                  Zuora environment to execute on  [default:\n                                  local]\n  --help                          Show this message and exit.\n```\n\n#### Bearer\n```\nUsage: zacc bearer [OPTIONS]\n\n  Prints bearer than exits\n\nOptions:\n  -c, --config-filename PATH      Config file containing Zuora ouath\n                                  credentials  [default: zuora_oauth.ini]\n  -e, --environment [prod|preprod|local]\n                                  Zuora environment to execute on  [default:\n                                  local]\n  --help                          Show this message and exit.\n```\n\n# Useful stuff\nHas a lot of graphs on Resource relationships:\nhttps://community.zuora.com/t5/Engineering-Blog/AQUA-An-Introduction-to-Join-Processing/ba-p/13262\n',
    'author': 'Janos Molnar',
    'author_email': 'janosmolnar1001@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/molnarjani/zuora-aqua-client-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
