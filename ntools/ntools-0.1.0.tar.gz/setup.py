# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ntools']

package_data = \
{'': ['*']}

install_requires = \
['attrs', 'click']

entry_points = \
{'console_scripts': ['ntools = ntools.cli:cli']}

setup_kwargs = {
    'name': 'ntools',
    'version': '0.1.0',
    'description': '',
    'long_description': '========\nOverview\n========\n\n.. start-badges\n\n.. list-table::\n    :stub-columns: 1\n\n    * - docs\n      - |docs|\n    * - tests\n      - | |travis|\n        | |codecov|\n    * - package\n      - | |version| |wheel| |supported-versions| |supported-implementations|\n        | |commits-since|\n\n.. |docs| image:: https://readthedocs.org/projects/ntools/badge/?style=flat\n    :target: https://readthedocs.org/projects/ntools\n    :alt: Documentation Status\n\n\n.. |travis| image:: https://travis-ci.com/python-metatooling/ntools.svg?branch=master\n    :alt: Travis-CI Build Status\n    :target: https://travis-ci.com/python-metatooling/ntools\n\n.. |codecov| image:: https://codecov.io/github/python-metatooling/ntools/coverage.svg?branch=master\n    :alt: Coverage Status\n    :target: https://codecov.io/github/python-metatooling/ntools\n\n.. |version| image:: https://img.shields.io/pypi/v/ntools.svg\n    :alt: PyPI Package latest release\n    :target: https://pypi.org/pypi/ntools\n\n.. |commits-since| image:: https://img.shields.io/github/commits-since/python-metatooling/ntools/v0.1.0.svg\n    :alt: Commits since latest release\n    :target: https://github.com/python-metatooling/ntools/compare/v0.1.0...master\n\n.. |wheel| image:: https://img.shields.io/pypi/wheel/ntools.svg\n    :alt: PyPI Wheel\n    :target: https://pypi.org/pypi/ntools\n\n.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/ntools.svg\n    :alt: Supported versions\n    :target: https://pypi.org/pypi/ntools\n\n.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/ntools.svg\n    :alt: Supported implementations\n    :target: https://pypi.org/pypi/ntools\n\n\n.. end-badges\n\nSome tools. How many? n.\n\n* Free software: MIT License\n\nInstallation\n============\n\n::\n\n    pip install ntools\n\nDocumentation\n=============\n\n\nhttps://ntools.readthedocs.io/\n\n\nDevelopment\n===========\n\nTo run the all tests run::\n\n    tox\n\nNote, to combine the coverage data from all the tox environments run:\n\n.. list-table::\n    :widths: 10 90\n    :stub-columns: 1\n\n    - - Windows\n      - ::\n\n            set PYTEST_ADDOPTS=--cov-append\n            tox\n\n    - - Other\n      - ::\n\n            PYTEST_ADDOPTS=--cov-append tox\n',
    'author': 'metatooling',
    'author_email': 'metatooling@cordaz.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
