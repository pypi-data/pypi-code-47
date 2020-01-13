# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['momba',
 'momba.ext',
 'momba.ext.jani',
 'momba.kit',
 'momba.model',
 'momba.moml',
 'momba.semantics',
 'momba.utils']

package_data = \
{'': ['*'],
 'momba.kit': ['.mypy_cache/3.8/*',
               '.mypy_cache/3.8/collections/*',
               '.mypy_cache/3.8/importlib/*',
               '.mypy_cache/3.8/os/*'],
 'momba.moml': ['.mypy_cache/3.8/*',
                '.mypy_cache/3.8/collections/*',
                '.mypy_cache/3.8/importlib/*',
                '.mypy_cache/3.8/json/*',
                '.mypy_cache/3.8/momba/*',
                '.mypy_cache/3.8/momba/ext/*',
                '.mypy_cache/3.8/momba/ext/jani/*',
                '.mypy_cache/3.8/momba/kit/*',
                '.mypy_cache/3.8/momba/model/*',
                '.mypy_cache/3.8/momba/moml/*',
                '.mypy_cache/3.8/momba/utils/*',
                '.mypy_cache/3.8/os/*']}

entry_points = \
{'console_scripts': ['moml = momba.moml.__main__:main']}

setup_kwargs = {
    'name': 'momba',
    'version': '0.1.4.dev0',
    'description': 'A Python library for quantitative models.',
    'long_description': "Momba\n=====\n\n|pypi| |build| |coverage| |docs| |black|\n\n**Momba is still in its early stages of development.\nPlease expect things to break.\nThe API is unstable and might change without further notice and deprecation period.**\n\n*Momba* is a Python library for working with quantitative models.\nMomba's core modeling formalism are networks of interacting *stochastic hybrid automata* (SHA) as per the `JANI specification`_.\nMomba aims to be a platform for prototyping and the development of new techniques and algorithms for the analysis of quantitative models.\nFor the time being, Momba does not aim to be a model checker itself.\nInstead, Momba relies on external tools for model checking via the JANI interaction protocol. In particular, Momba works well with `The Modest Toolset`__ and `EPMC`__.\n\n__ http://www.modestchecker.net/\n__ https://github.com/ISCAS-PMC/ePMC\n\n.. _JANI specification: http://www.jani-spec.org/\n\n\nHow to use Momba?\n-----------------\nPlease read `the documentation`_.\n\n.. _the documentation: https://depend.cs.uni-saarland.de/~koehl/momba/\n\n\n.. |pypi| image:: https://img.shields.io/pypi/v/momba.svg?label=latest%20version\n    :target: https://pypi.python.org/pypi/momba\n\n.. |build| image:: https://dgit.cs.uni-saarland.de/koehlma/momba/badges/master/pipeline.svg\n    :target: https://dgit.cs.uni-saarland.de/koehlma/momba/pipelines\n\n.. |coverage| image:: https://dgit.cs.uni-saarland.de/koehlma/momba/badges/master/coverage.svg\n    :target: https://dgit.cs.uni-saarland.de/koehlma/momba/pipelines\n\n.. |docs| image:: https://img.shields.io/static/v1?label=docs&message=master&color=blue\n    :target: https://depend.cs.uni-saarland.de/~koehl/momba/\n\n.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/psf/black\n",
    'author': 'Maximilian Köhl',
    'author_email': 'mkoehl@cs.uni-saarland.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://depend.cs.uni-saarland.de/~koehl/momba/',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
