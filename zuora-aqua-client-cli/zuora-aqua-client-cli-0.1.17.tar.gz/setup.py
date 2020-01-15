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
    'version': '0.1.17',
    'description': 'Run ZOQL queries through AQuA from the command line',
    'long_description': '# zuora-aqua-client-cli [![Build Status](https://travis-ci.com/molnarjani/zuora-aqua-client-cli.svg?branch=master)](https://travis-ci.com/molnarjani/zuora-aqua-client-cli)\n\nRun ZOQL queries through AQuA from the command line\n\n\n# Installation\n\n#### Mac\n`pip3 install zuora-aqua-client-cli`\nThe executable will be installed to `/usr/local/bin/zacc`\n\n#### Linux\n`pip3 install zuora-aqua-client-cli`\nThe executable will be installed to `~/.local/bin/zacc`\n\nMake sure `~/.local/bin/` is added to your `$PATH`\n\n# Configuration\nConfiguration should be provided by the `-c /path/to/file` option.\n\n#### Example config\n```\n[prod]\nproduction = true\nclient_id = <client_id>\nclient_secret = <client_secret>\n\n[sandbox]\nproduction = false\nclient_id = <client_id>\nclient_secret = <client_secret>\n```\n\n# Usage\n\n#### Cheatsheet\n```\n# List fiels for resource\n$ zacc describe -c ~/.config.ini -e sandbox Account\nAccount\n  AccountNumber - Account Number\n  AdditionalEmailAddresses - Additional Email Addresses\n  AllowInvoiceEdit - Allow Invoice Editing\n  AutoPay - Auto Pay\n  Balance - Account Balance\n  ...\nRelated Objects\n  BillToContact<Contact> - Bill To\n  DefaultPaymentMethod<PaymentMethod> - Default Payment Method\n  ParentAccount<Account> - Parent Account\n  SoldToContact<Contact> - Sold To\n\n# Request a bearer token, then exit\n$ zacc bearer -c ~/.config.ini -e sandbox\nBearer <bearer token>\n\n# Execute an AQuA job\n$ zacc query -c ~/.config.ini -e sandbox -z "select Account.Name from Account where Account.CreatedDate > \'2019-01-10\'"\nAccount.Name\nJohn Doe\nJane Doe\n\n# Execute an AQuA job from a ZOQL query file\n$ zacc query -c ~/.config.ini -e sandbox -z ~/query_names.zoql\nAccount.Name\nJohn Doe\nJane Doe\n```\n\n#### Zacc\n```\nUsage: zacc [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  bearer    Prints bearer than exits\n  describe  List available fields of Zuora resource\n  query     Run ZOQL Query\n```\n\n#### Query\n```\nUsage: zacc query [OPTIONS]\n\n  Run ZOQL Query\n\nOptions:\n  -c, --config-filename PATH      Config file containing Zuora ouath\n                                  credentials  [default: zuora_oauth.ini]\n  -z, --zoql PATH                 ZOQL file to be executed  [default:\n                                  input.zoql]\n  -o, --output PATH               Where to write the output to, default is\n                                  STDOUT\n  -e, --environment [prod|preprod|local]\n                                  Zuora environment to execute on  [default:\n                                  local]\n  -m, --max-retries INTEGER       Maximum retries for query\n  --help                          Show this message and exit.\n```\n\n#### Describe\n```\nUsage: zacc describe [OPTIONS] RESOURCE\n\n  List available fields of Zuora resource\n\nOptions:\n  -c, --config-filename PATH      Config file containing Zuora ouath\n                                  credentials  [default: zuora_oauth.ini]\n  -e, --environment [prod|preprod|local]\n                                  Zuora environment to execute on  [default:\n                                  local]\n  --help                          Show this message and exit.\n```\n\n#### Bearer\n```\nUsage: zacc bearer [OPTIONS]\n\n  Prints bearer than exits\n\nOptions:\n  -c, --config-filename PATH      Config file containing Zuora ouath\n                                  credentials  [default: zuora_oauth.ini]\n  -e, --environment [prod|preprod|local]\n                                  Zuora environment to execute on  [default:\n                                  local]\n  --help                          Show this message and exit.\n```\n\n# Useful stuff\nHas a lot of graphs on Resource relationships:\nhttps://community.zuora.com/t5/Engineering-Blog/AQUA-An-Introduction-to-Join-Processing/ba-p/13262\n',
    'author': 'Janos Molnar',
    'author_email': 'janosmolnar1001@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/molnarjani/zuora-aqua-client-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
