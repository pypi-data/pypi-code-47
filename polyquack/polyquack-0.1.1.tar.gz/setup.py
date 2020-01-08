# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['polyquack']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'polyquack',
    'version': '0.1.1',
    'description': 'utilities for polyglots',
    'long_description': '# polyquack\n\n## Preamble\n\n`polyquack` is a utility (possibly part of a larger set in the future) for pluralizing words based on rules of varying complexity.\n\nIt has been inspired by the [*Localization and Plurals* page](https://developer.mozilla.org/en-US/docs/Mozilla/Localization/Localization_and_Plurals) from the MDN.\n\n## Installation\n\nSimply run `pip install polyquack`.\n\n## Usage\n\nFirst, define a list of forms. It is a simple `dict` with language codes as keys. For now, refer to the `tests/test_pluralization.py` file to see the form definitions by rule, and the `rules.py` file for a mapping of languages to rules. Not all languages have the same number of forms (for instance, slavic languages often have a genitive plural form).\n\n    >>> song_forms = {\n    ...     "en": ["song", "songs"],\n    ...     "fr": ["chanson", "chansons"],\n    ...     "pl": ["piosenka", "piosenki", "piosenek"],\n    ... }\n\nThis package provides a handy `Pluralizable` class that you can use.\n\n    >>> from polyquack import pluralization\n    >>> song = pluralization.Pluralizable(forms=song_forms)\n    >>> print(f"4 {song.pluralize_by_language(\'pl\', 4)}") # nominative plural\n    4 piosenki\n    >>> print(f"5 {song.pluralize_by_language(\'pl\', 5)}") # genitive plural\n    5 piosenek\n\n## Todo\n\nThis project is barely a few days old. I will be adding proper documentation, and `tox` for testing.',
    'author': 'Patryk Bratkowski',
    'author_email': 'git@patryk.tech',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/patryk-media/polyquack',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
