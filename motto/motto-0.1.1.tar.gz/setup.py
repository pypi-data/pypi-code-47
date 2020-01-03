# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['motto', 'motto.core', 'motto.skills']

package_data = \
{'': ['*']}

install_requires = \
['click-default-group>=1.2.2,<2.0.0',
 'click>=7.0,<8.0',
 'docutils>=0.15.2,<0.16.0',
 'janome>=0.3.10,<0.4.0',
 'typing-extensions>=3.7.4,<4.0.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses>=0.7,<0.8']}

entry_points = \
{'console_scripts': ['motto = motto.cli:main']}

setup_kwargs = {
    'name': 'motto',
    'version': '0.1.1',
    'description': 'Japanese sentence linter platform for reStructuredText',
    'long_description': 'motto\n=====\n\n.. image:: https://img.shields.io/pypi/v/motto\n   :alt: PyPI\n   :target: https://pypi.org/project/motto\n\n.. image:: https://img.shields.io/pypi/pyversions/motto\n   :alt: PyPI - Python Version\n   :target: https://pypi.org/project/motto\n\n.. image:: https://github.com/attakei/motto/workflows/Continuous%20Integration/badge.svg?branch=master\n   :alt: GitHub Actions - Continuous Integration\n   :target: https://github.com/attakei/motto/actions\n\ndocutils-based sentence linter.\n\nOverview\n--------\n\nMotto is sentence linter platform for reStructuredText.\n\nIt parses document by ``docutils`` and check any paragraph by linter modules.\n\nDemo\n----\n\n.. image:: https://attakei.net/assets/motto/motto-demo.gif\n\nInstallation\n------------\n\nYou can install by ``pip`` command.\n\n.. code-block:: bash\n\n   pip install motto\n\nUsage\n-----\n\nRun ``motto`` command.\n\n.. code-block:: bash\n\n   # Check single file\n   motto README.rst\n   # Checke internals of directory recursively\n   motto docs/\n\nMore information\n----------------\n\nSee `Janapanese readme document <./README_ja.rst>`_\n\nLicense\n-------\n\nMIT License. See `it <./LICENSE>`_\n',
    'author': 'Kazuya Takei',
    'author_email': 'attakei@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
