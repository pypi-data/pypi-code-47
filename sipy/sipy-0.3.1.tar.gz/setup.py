# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sipy', 'sipy.quantities', 'sipy.units']

package_data = \
{'': ['*']}

install_requires = \
['toml>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'sipy',
    'version': '0.3.1',
    'description': '',
    'long_description': "|build| |coverage| |pypi| |python| |license|\n\nSIpy\n====\n\nSIpy is a fast, lightweight and easily extensible python package for manipulating\nphysical quantities.\n\nFor more detailed information read the `documentation <https://broster.gitlab.io/sipy/>`_.\n\nQuickstart\n==========\nSIpy can be installed via `pipenv\n<https://docs.pipenv.org/install/#installing-packages-for-your-project>`_ or\n`pip <https://docs.python.org/3/installing/index.html>`_, and requires Python 3.6.0 or higher.\n\n.. code-block:: console\n\n    $ pipenv install sipy\n    $ pip install sipy\n\nOnce SIpy is installed just import the quantities you need and you're good to go\n\n.. code-block:: python\n\n    >>> from sipy import miles, hour\n    >>> speed_limit = 70 * miles / hour\n    >>> print(speed_limit)\n    3.13E+01ms^-1\n\n\nContributing\n============\n\nSIpy is developed on `GitLab\n<https://gitlab.com/broster/sipy>`_. If you come across an issue,\nor have a feature request please open an `issue\n<https://gitlab.com/broster/sipy/issues>`_.  If you want to\ncontribute a fix or feature-implementation please do by proposing a `merge request\n<https://gitlab.com/broster/sipy/merge_requests>`_.\n\nTesting\n~~~~~~~\n\nSIpy uses `Pytest <https://docs.pytest.org/en/latest/>`_ for unit testing and\nand `pre-commit <https://pre-commit.com/>`_ for static analysis and auto-formatting.\nCode is automatically checked by Gitlab pipelines when pushed but it is\nrecommended that tests are also run locally.\n\nSIpy used `Poetry <https://python-poetry.org/>`_ for managing all external dependencies.\nInstall `Poetry` using the instructions `here <https://python-poetry.org/docs/>`_ and then\ninstall dependencies with\n\n.. code-block:: console\n\n    $ poetry install\n\n`pre-commit` should run automatically on every commit. To enable it run\n\n.. code-block:: console\n\n    $ poetry run pre-commit install\n\nThe unittests can be run with:\n\n.. code-block:: console\n\n    $ poetry run pytest --doctest-modules tests sipy README.rst\n\nHelp\n====\n\nThe SIpy `documentation <https://broster.gitlab.io/sipy/>`_\nis the best place to start, after that try searching stack overflow,\nif you still can't find an answer please `open an issue\n<https://broster.gitlab.io/sipy/issues>`_.\n\n\n.. |build| image:: https://gitlab.com/broster/sipy/badges/master/pipeline.svg\n   :target: https://gitlab.com/broster/sipy/commits/master\n\n.. |coverage| image:: https://gitlab.com/broster/sipy/badges/master/coverage.svg\n   :target: https://gitlab.com/broster/sipy/commits/master\n\n.. |pypi| image:: https://img.shields.io/pypi/v/sipy.svg\n   :target: https://pypi.python.org/pypi/Hypercorn/\n\n.. |python| image:: https://img.shields.io/pypi/pyversions/sipy.svg\n   :target: https://pypi.python.org/pypi/Hypercorn/\n\n.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg\n   :target: https://gitlab.com/pgjones/hypercorn/blob/master/LICENSE\n",
    'author': 'Samuel Broster',
    'author_email': 's.h.broster+gitlab@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://broster.gitlab.io/sipy/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
