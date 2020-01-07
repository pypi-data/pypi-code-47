# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['syntactic']

package_data = \
{'': ['*']}

modules = \
['syntactic_installer', '__syntax__']
install_requires = \
['importlib_metadata']

entry_points = \
{'console_scripts': ['syntactic = syntactic.cli:cli'],
 'syntactic.transformers': ['bangbang_means_hello = '
                            'syntactic.examples:transform_bangbang',
                            'unicode_lambda = '
                            'syntactic.examples:transform_lambda']}

setup_kwargs = {
    'name': 'syntactic',
    'version': '0.1.2',
    'description': 'Custom syntax for Python.',
    'long_description': "========\nOverview\n========\n\n.. start-badges\n\n.. list-table::\n    :stub-columns: 1\n\n    * - docs\n      - |docs|\n    * - tests\n      - | |travis|\n        | |codecov|\n    * - package\n      - | |version| |wheel| |supported-versions| |supported-implementations|\n        | |commits-since|\n\n.. |docs| image:: https://img.shields.io/readthedocs/syntactic\n    :target: https://readthedocs.org/projects/syntactic\n    :alt: Documentation Status\n\n\n.. |travis| image:: https://img.shields.io/travis/com/metatooling/python-syntactic\n    :alt: Travis-CI Build Status\n    :target: https://travis-ci.com/metatooling/syntactic\n\n.. |codecov| image:: https://codecov.io/github/metatooling/syntactic/coverage.svg\n    :alt: Coverage Status\n    :target: https://codecov.io/github/metatooling/syntactic\n\n.. |version| image:: https://img.shields.io/pypi/v/syntactic.svg\n    :alt: PyPI Package latest release\n    :target: https://pypi.org/pypi/syntactic\n\n.. |commits-since| image:: https://img.shields.io/github/commits-since/metatooling/syntactic/v0.1.2.svg\n    :alt: Commits since latest release\n    :target: https://github.com/metatooling/syntactic/compare/v0.1.2...master\n\n.. |wheel| image:: https://img.shields.io/pypi/wheel/syntactic.svg\n    :alt: PyPI Wheel\n    :target: https://pypi.org/pypi/syntactic\n\n.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/syntactic.svg\n    :alt: Supported versions\n    :target: https://pypi.org/pypi/syntactic\n\n.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/syntactic.svg\n    :alt: Supported implementations\n    :target: https://pypi.org/pypi/syntactic\n\n\n.. end-badges\n\n\nhttps://syntactic.readthedocs.io/\n\nCustomizable syntax for Python.\n\nPossible uses\n==================\n\n- Experimenting with possible language features.\n- Boilerplate reduction.\n\n\n\n\n\nExamples\n==========\n\nUnicode lambdas\n-------------------\n\n.. code-block:: python\n\n    from __syntax__ import unicode_lambda\n\n    func = λx: x + 1\n\nis equivalent to\n\n.. code-block:: python\n\n    func = lambda x: x + 1\n\nSQL template literals\n------------------------\n\nEmbedded sql:\n\n.. code-block:: js\n\n  from __syntax__ import sql_literals\n\n  engine.query(sql`SELECT author FROM books WHERE name = {book} AND author = {author}`)\n\nis equivalent to:\n\n.. code-block:: python\n\n    engine.query('SELECT author FROM books WHERE name = ? AND author = ?', [book, author])\n\n\nLimitations\n===============\n\nThe example transformers are written in a fragile way. They are intended only as\ninspiration rather than production-ready transformers. If you want to add some\nproduction-ready ones, pull-requests are welcome.\n\n\n\n\nRelated work\n===================\n\nSeveral projects have explored manipulating Python syntax.\n\n- MacroPy_\n- future-fstrings_\n- experimental_\n\n.. _MacroPy:  http://macropy3.readthedocs.io/en/latest/\n.. _future-fstrings: https://github.com/asottile/future-fstrings\n.. _experimental: https://github.com/aroberge/experimental\n",
    'author': 'Metatooling',
    'author_email': 'metatooling@cordaz.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
