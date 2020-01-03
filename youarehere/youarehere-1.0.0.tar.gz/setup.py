# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['youarehere']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.10.43,<2.0.0', 'click>=7.0,<8.0', 'requests>=2.22.0,<3.0.0']

entry_points = \
{'console_scripts': ['youarehere = youarehere:cli']}

setup_kwargs = {
    'name': 'youarehere',
    'version': '1.0.0',
    'description': 'Route53 DNS utility',
    'long_description': '# you are here \xf0\x9f\x8c\x8e\n\n![PyPI - License](https://img.shields.io/pypi/l/youarehere?style=for-the-badge) ![PyPI](https://img.shields.io/pypi/v/youarehere?style=for-the-badge) ![](https://img.shields.io/badge/PRETTY%20DOPE-\xf0\x9f\x91\x8d-blue?style=for-the-badge)\n\nSomehow, adding a new record to Route53 takes 100 lines of Python. So now it only takes one.\n\n```python\n>>> from youarehere import create_record\n>>> create_record("A", "foo.example.com", "4.4.4.4")\n```\n\nYou can also easily point a record to the current machine:\n\n```python\n>>> from youarehere import point_record_to_here\n>>> point_record_to_here("foo.example.com")\n```\n\n## use case\n\nYou have a Raspberry Pi that travels around and you want to keep a pointer to it in Route53. Add this as a cron-job:\n\n```\n$ python3 -c "point_record_to_here(\'my-pi.example.com\')"\n```\n\n\n## `create_record` Arguments\n\n| Argument       | Type                | Default | Description                                                                                                                           |\n| -------------- | ------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |\n| record_type    | `str`               |         | The type of the record to add (e.g. A, CNAME, etc). For an exhaustive list, see `youarehere.VALID_RECORD_TYPES`.                      |\n| name           | `str`               |         | The DNS record name (e.g. `"foo.example.com"`)                                                                                        |\n| destination    | `str` / `List[str]` |         | The destination IP or values (e.g. `["4.4.4.4", "8.8.8.8"]`). If you provide a single string, it will be treated as an Array[1].      |\n| hosted_zone_id | `str`               | None    | ID of the hosted zone to which to add this record. Guess automatically by default, or use `youarehere.guess_hosted_zone_id_for_name`. |\n| comment        | `str`               | ""      | An optional comment for the change request (e.g. `"Baby\'s first DNS record!"`)                                                        |\n| ttl            | `int`               | 300     | The TTL for your record; defaults to 300 which is probably too low.                                                                   |\n\n---\n\n<small>Documentation auto-generated with [`docshund`](https://github.com/FitMango/docshund/), bork bork. \xf0\x9f\x90\x95</small>\n\n\n## CLI Usage\n\nExamples:\n\nPoint \'test.example.com\' to the current machine:\n\n    $ youarehere test.example.com\n\nPoint \'test.example.com\' to the IP 93.184.216.34\n\n    $ youarehere test.example.com 93.184.216.34\n\nPoint \'test.example.com\' to a set of IPs in descending order,\nwith a TTL of 6000 seconds.\n\n    $ youarehere test.example.com 93.184.216.34,93.184.216.35 --ttl 6000\n\n\n| Argument    | Description                                 |\n| ----------- | ------------------------------------------- |\n| name        | Record to add (e.g. "test.example.com")     |\n| destination | IP destination. Default: Current global IP. |\n\n| Flag      | Description                                   |\n| --------- | --------------------------------------------- |\n| --type    | (A) The type of record to add                 |\n| --ttl     | (300) The TTL of the new DNS record           |\n| --dry-run | (False) Print and quit without making changes |\n',
    'author': 'Jordan Matelsky',
    'author_email': 'j6k4m8@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/j6k4m8/youarehere',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
