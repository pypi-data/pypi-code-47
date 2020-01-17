# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyglint']

package_data = \
{'': ['*']}

install_requires = \
['attrs', 'public>=2019.4.13,<2020.0.0', 'pylint']

setup_kwargs = {
    'name': 'pyglint',
    'version': '0.1.3',
    'description': 'Pylint checkers made easy.',
    'long_description': '========\nOverview\n========\n\n.. start-badges\n\n.. list-table::\n    :stub-columns: 1\n\n    * - docs\n      - |docs|\n    * - tests\n      - | |travis|\n        | |codecov|\n    * - package\n      - | |version| |wheel| |supported-versions| |supported-implementations|\n        | |commits-since|\n\n.. |docs| image:: https://readthedocs.org/projects/pyglint/badge/?style=flat\n    :target: https://readthedocs.org/projects/pyglint\n    :alt: Documentation Status\n\n\n.. |travis| image:: https://travis-ci.com/metatooling/pyglint.svg?branch=master\n    :alt: Travis-CI Build Status\n    :target: https://travis-ci.com/metatooling/pyglint\n\n.. |codecov| image:: https://codecov.io/github/metatooling/pyglint/coverage.svg?branch=master\n    :alt: Coverage Status\n    :target: https://codecov.io/github/metatooling/pyglint\n\n.. |version| image:: https://img.shields.io/pypi/v/pyglint.svg\n    :alt: PyPI Package latest release\n    :target: https://pypi.org/pypi/pyglint\n\n.. |commits-since| image:: https://img.shields.io/github/commits-since/metatooling/pyglint/v0.1.3.svg\n    :alt: Commits since latest release\n    :target: https://github.com/metatooling/pyglint/compare/v0.1.3...master\n\n.. |wheel| image:: https://img.shields.io/pypi/wheel/pyglint.svg\n    :alt: PyPI Wheel\n    :target: https://pypi.org/pypi/pyglint\n\n.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pyglint.svg\n    :alt: Supported versions\n    :target: https://pypi.org/pypi/pyglint\n\n.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pyglint.svg\n    :alt: Supported implementations\n    :target: https://pypi.org/pypi/pyglint\n\n\n.. end-badges\n\nMakes it easy to write custom Pylint checkers.\n\nInstallation\n============\n\n::\n\n    pip install pyglint\n\nDocumentation\n=============\n\n\nhttps://pyglint.readthedocs.io/\n',
    'author': 'metatooling',
    'author_email': 'metatooling@cordaz.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
