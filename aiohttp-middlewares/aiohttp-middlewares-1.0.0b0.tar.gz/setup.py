# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiohttp_middlewares']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.5,<4.0', 'async-timeout>=1.2,<4']

setup_kwargs = {
    'name': 'aiohttp-middlewares',
    'version': '1.0.0b0',
    'description': 'Collection of useful middlewares for aiohttp applications.',
    'long_description': '===================\naiohttp-middlewares\n===================\n\n.. image:: https://img.shields.io/circleci/project/github/playpauseandstop/aiohttp-middlewares/master.svg\n    :target: https://circleci.com/gh/playpauseandstop/aiohttp-middlewares\n    :alt: CircleCI\n\n.. image:: https://img.shields.io/pypi/v/aiohttp-middlewares.svg\n    :target: https://pypi.org/project/aiohttp-middlewares/\n    :alt: Latest Version\n\n.. image:: https://img.shields.io/pypi/pyversions/aiohttp-middlewares.svg\n    :target: https://pypi.org/project/aiohttp-middlewares/\n    :alt: Python versions\n\n.. image:: https://img.shields.io/pypi/l/aiohttp-middlewares.svg\n    :target: https://github.com/playpauseandstop/aiohttp-middlewares/blob/master/LICENSE\n    :alt: BSD License\n\n.. image:: https://coveralls.io/repos/playpauseandstop/aiohttp-middlewares/badge.svg?branch=master&service=github\n    :target: https://coveralls.io/github/playpauseandstop/aiohttp-middlewares\n    :alt: Coverage\n\n.. image:: https://readthedocs.org/projects/aiohttp-middlewares/badge/?version=latest\n    :target: http://aiohttp-middlewares.readthedocs.org/en/latest/\n    :alt: Documentation\n\nCollection of useful middlewares for `aiohttp <http://aiohttp.readthedocs.org/>`_\napplications.\n\n- Works on Python 3.6+\n- Works with aiohttp 3.5+\n- BSD licensed\n- Latest documentation `on Read The Docs\n  <https://aiohttp-middlewares.readthedocs.io/>`_\n- Source, issues, and pull requests `on GitHub\n  <https://github.com/playpauseandstop/aiohttp-middlewares>`_\n\nQuickstart\n==========\n\nBy default ``aiohttp.web`` does not provide many built-in middlewares for\nstandart web development actions such as handling errors, shielding view\nhandlers, or providing CORS headers.\n\n``aiohttp-middlewares`` fix this by providing several middlewares that aims to\ncover most common web-development needs.\n\nFor example, to enable CORS headers for ``http://localhost:8081`` and handle\nerrors for ``aiohttp.web`` application you need to,\n\n.. code-block:: python\n\n    from aiohttp import web\n    from aiohttp_middlewares import cors_middleware, error_middleware\n\n\n    app = web.Application(\n        middlewares=(\n            cors_middleware(origins=("http://localhost:8081",)),\n            error_middleware(),\n        )\n    )\n\nCheck `documentation <https://aiohttp-middlewares.readthedocs.io/>`_ for\nall available middlewares and available initialization options.\n',
    'author': 'Igor Davydenko',
    'author_email': 'iam@igordavydenko.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://igordavydenko.com/projects.html#aiohttp-middlewares',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
