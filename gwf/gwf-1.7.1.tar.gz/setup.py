# -*- coding: utf-8 -*-
from distutils.core import setup

package_dir = \
{'': 'src'}

packages = \
['gwf', 'gwf.backends', 'gwf.plugins']

package_data = \
{'': ['*']}

install_requires = \
['click-plugins>=1.0,<2.0', 'click>=6.0,<7.0']

entry_points = \
{'console_scripts': ['gwf = gwf.cli:main'],
 'gwf.backends': ['local = gwf.backends.local:LocalBackend',
                  'sge = gwf.backends.sge:SGEBackend',
                  'slurm = gwf.backends.slurm:SlurmBackend',
                  'testing = gwf.backends.testing:TestingBackend'],
 'gwf.plugins': ['cancel = gwf.plugins.cancel:cancel',
                 'clean = gwf.plugins.clean:clean',
                 'config = gwf.plugins.config:config',
                 'info = gwf.plugins.info:info',
                 'init = gwf.plugins.init:init',
                 'logs = gwf.plugins.logs:logs',
                 'run = gwf.plugins.run:run',
                 'status = gwf.plugins.status:status',
                 'touch = gwf.plugins.touch:touch',
                 'workers = gwf.plugins.workers:workers']}

setup_kwargs = {
    'name': 'gwf',
    'version': '1.7.1',
    'description': 'A flexible, pragmatic workflow tool.',
    'long_description': "===\ngwf\n===\n\nA flexible, pragmatic workflow tool.\n\n|anacondaversion| |anacondadownloads| |cistatus| |coveralls|\n\n*gwf* is a flexible, pragmatic workflow tool for building and running large,\nscientific workflows. It runs on Python 3.5+ and is developed at the\nBioinformatics Research Centre (BiRC), Aarhus University.\n\nExamples\n  To get a feeling for what a *gwf* workflow looks like, have a look at a few\n  `examples`_.\n\nGetting started\n  To quickly get started writing workflows in *gwf* you can read the\n  `User's Guide`_.\n\nExtending\n  We don't have the backend you need to run your workflow on your cluster?\n  See the `Writing Backends`_ section to roll your own.\n\nContributing\n  We aim to make *gwf* a community developed project. Learn how to\n  `contribute`_.\n\n.. _examples: https://github.com/gwforg/gwf/tree/master/examples\n.. _User's Guide: https://gwf.app/guide/tutorial/\n.. _Writing Backends: https://gwf.app/development/writingbackends/\n.. _contribute: https://gwf.app/development/forcontributors/\n\n\n.. |cistatus| image:: https://img.shields.io/travis/gwforg/gwf.svg\n    :target: https://travis-ci.org/gwforg/gwf\n    :alt: Build status\n.. |coveralls| image:: https://img.shields.io/coveralls/gwforg/gwf.svg\n    :target: https://coveralls.io/github/gwforg/gwf\n    :alt: Coverage\n.. |anacondaversion| image:: https://anaconda.org/gwforg/gwf/badges/version.svg\n    :target: https://anaconda.org/gwforg/gwf\n    :alt: Version of Conda package\n.. |anacondadownloads| image:: https://anaconda.org/gwforg/gwf/badges/downloads.svg\n    :target: https://anaconda.org/gwforg/gwf\n    :alt: Downloads with Conda\n",
    'author': 'Dan Søndergaard',
    'author_email': 'das@birc.au.dk',
    'url': 'https://github.com/gwforg/gwf',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
