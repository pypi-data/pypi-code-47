# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pydrugshortagesca']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'click_config_file>=0.5.0,<0.6.0',
 'configobj>=5.0.6,<6.0.0',
 'requests>=2.22.0,<3.0.0']

entry_points = \
{'console_scripts': ['pydrugshortagesca = pydrugshortagesca.cli:run']}

setup_kwargs = {
    'name': 'pydrugshortagesca',
    'version': '0.1.1',
    'description': 'Minimal Python wrapper for the drugshortagescanada.ca database API',
    'long_description': '# pydrugshortagesca\n\nA minimal python wrapper around the [drugshortagescanada.ca](https://drugshortagescanada.ca) database API\n\nDepends on `requests` module and will pass through exceptions from that library when they occur. \n\n## Installation\n\nInstall the package: \n\n```\npip install pydrugshortagesca\n```\n\nYou can then configure your `drugshortagescanada.ca` username and password in one of the following ways: \n\nCreate configuration file in `~/.config/pydrugshortagesca/config`:\n\n```sh\nemail="username@domain.com"\npassword="s3cr3t!"\n```\n\nOr, set the following environment variables: \n\n```sh\nexport DSC_EMAIL="username@domain.com"\nexport DSC_PASSWORD="s3cr3t!"\n```\n\nYou can test your installation by running the command `pydrugshortagesca`. You\nshould not be prompted for a username or password, and it should return some\nresults in JSON format. \n\n## Basic Usage\n\nInteracting with the `drugshortagescanada.ca` database is done via the\n`api.Session` object: \n\n```python\nfrom pydrugshortagesca import api, export\nimport json\n\nsession = api.Session(email="name@domain.com", password="123456")\n\ntry:\n\tsession.login()\nexcept Exception as e:\n\tprint("Error with log in", e)\n\tprint("Details:", session.response.content)\nelse: \n\t# search() returns a batch of results.\n    # Use the `limit` and `offset` parameters to adjust which batch to return.\n\tjson_results = session.search(term="venlafaxine", offset=20)\n\tprint("Total results {}".format(json_results[\'total\']))\n\n\t# isearch() returns an iterator over all records returned by a search.\n    # This may make several requests to the database if needed.\n\tresults = session.isearch(term="venlafaxine", orderby=\'updated_date\')\n\tfor rec in results:\n\t\tprint(rec[\'updated_date\'],rec[\'en_drug_brand_name\'],rec[\'drug_strength\'])\n\n\t# Custom filter functions can also be supplied\n\tresults = session.isearch(_filter=lambda x: x[\'drug_strength\'] == \'150.0MG\',\n\t\tterm="venlafaxine", orderby=\'updated_date\'):\n\tfor rec in results:\n\t\tprint(rec[\'updated_date\'],rec[\'en_drug_brand_name\'],rec[\'drug_strength\'])\n\t\n\t# The export module provides utility functions for exporting results in tabular form\n\tcsvfile = open(\'shortages.csv\',\'w\')\n\texport.as_csv(session, csvfile, shortages=True, term="venlafaxine")\n```\n\n## CLI \n\nThere is also a commandline interface. See `pydrugshortagesca --help` for details, but briefly:\n\n```sh\n$ pydrugshortagesca -p term venlafaxine --type shortages --fmt csv > shortages.csv\n```\n\n## License\n\nMIT\n\n## Contributing\n\nPull requests are very welcome!\n',
    'author': 'Jon Pipitone',
    'author_email': 'jon@pipitone.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pipitone/pydrugshortagesca',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
