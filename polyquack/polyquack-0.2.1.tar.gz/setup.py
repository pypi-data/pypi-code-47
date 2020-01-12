# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['polyquack']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'polyquack',
    'version': '0.2.1',
    'description': 'utilities for polyglots',
    'long_description': '# polyquack\n\n## Preamble\n\n`polyquack` is a set of utilities for pluralizing words based on rules of varying complexity, and translating words or longer texts.\n\nThe pluralization module has been inspired by the [*Localization and Plurals* page](https://developer.mozilla.org/en-US/docs/Mozilla/Localization/Localization_and_Plurals) from the MDN.\n\n## Installation\n\nSimply run `pip install polyquack`.\n\n## Usage\n\nSee the [polyquack documentation](https://patryk-media.gitlab.io/polyquack/docs/) for usage instructions.\n',
    'author': 'Patryk Bratkowski',
    'author_email': 'git@patryk.tech',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://patryk-media.gitlab.io/polyquack/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
