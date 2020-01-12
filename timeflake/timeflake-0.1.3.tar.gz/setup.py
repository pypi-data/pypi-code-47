# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['timeflake']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'timeflake',
    'version': '0.1.3',
    'description': 'Timeflakes are 64-bit roughly-ordered, globally-unique, URL-safe UUIDs.',
    'long_description': "# timeflake\nTimeflakes are 64-bit (unsigned), roughly-ordered, URL-safe UUIDs. Inspired by Twitter's Snowflake and Instagram's UUID.\n\nIt supports incremental sequence per shard ID, and cryptographically strong pseudo-random numbers.\n\nThe IDs store the following in binary form (in this order):\n- Time since custom epoch in seconds (32 bits).\n- Logical shard ID (10 bits).\n- Sequence number (22 bits).\n\n## Example\n\n```python\ntimeflake = Timeflake()\ntimeflake.random()\n>>> 'eihdZ7Hqa'\n```\n\nThe resulting string `efqCcXufN` contains the following information:\n```\nuint64 = 4085399177663909\ntimestamp = 1578784406\nshard_id = 123\nsequence_number = 5541\n```\n\n## Properties\n\nSome nice properties of having an auto-incrementing sequence as the most significant part of the resulting ID are:\n- Reduced performance impact when using clustered indices on relational databases (vs random UUIDs).\n- The IDs are (roughly) sortable, so you can tell if one ID was created a few seconds before or after another.\n\nThe `.random()` method returns a new UUID using cryptographically strong pseudo-random numbers for the sequence number.\n\nWhen using the random method, the probability of a collision per logical shard per second is `0.00000024` (about 1 in 4 million). If you do not specify the `shard_id`, a random one will be selected for you.\n\nYou can also use the `.next()` method to use an auto-incrementing number for the sequence number:\n\n```python\ntimeflake = Timeflake(shard_id=7)\ntimeflake.next()\n>>> 'eicbZeGxe'\n# uint64=4090831824755682 timestamp=1578785671 shard_id=7 sequence_number=7138\n```\n\n\nBy default they are encoded in base57 for (nice) URL-safe representation. This means they are concise (max length of 11 characters).\n\nIf you prefer to work with the unsigned 64-bit integer form, simply pass `encoding='uint64'` to the instance:\n\n```python\ntimeflake = Timeflake(encoding='uint64')\ntimeflake.random()\n>>> 4085399177663909\n```\n\nThe default alphabet for base57 encoding is: `23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz`. It intentionally removes visually similar characters (like 1 and l) while keeping the resulting ID short with a max of 11 characters.\n\nWhen using the default epoch (2020-01-01), the IDs will run out at around 2088-01-19.\n\n## Supported versions\nI'll be adding tests for various python versions. But I only intend to support Python 3.7+ at this moment.\n\n## Dependencies\nNo dependencies other than the standard library.\n\n## Contribute\nWant to hack on the project? Any kind of contribution is welcome!\nSimply follow the next steps:\n\n- Fork the project.\n- Create a new branch.\n- Make your changes and write tests when practical.\n- Commit your changes to the new branch.\n- Send a pull request, it will be reviewed shortly.\n- In case you want to add a feature, please create a new issue and briefly explain what the feature would consist of. For bugs or requests, before creating an issue please check if one has already been created for it.\n\n## Changelog\nPlease see the [changelog](CHANGELOG.md) for more details.\n\nLicense\nThis project is licensed under the MIT license. Please read the [LICENSE](LICENSE) file for more details.",
    'author': 'Anthony Najjar Simon',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/anthonynsimon/timeflake',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
