# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['testrunner', 'testrunner.runners']

package_data = \
{'': ['*']}

install_requires = \
['attr>=0.3.1,<0.4.0',
 'benchexec>=2.5,<3.0',
 'deprecated>=1.2,<2.0',
 'pipfile>=0.0.2,<0.0.3',
 'plumbum>=1.6,<2.0',
 'pytesting-utils>=0.5.0,<0.6.0',
 'virtualenv>=16.7,<17.0']

setup_kwargs = {
    'name': 'test-runner',
    'version': '0.7.0',
    'description': 'A small test runner library for Python testing',
    'long_description': "# test-runner—A Runner for Python Tests\n\n[![Build Status](https://travis-ci.com/pytesting/test-runner.svg?token=ZgCiES6Mybgq3a2Jbw2K&branch=master)](https://travis-ci.com/pytesting/test-runner)\n[![codecov](https://codecov.io/gh/pytesting/test-runner/branch/master/graph/badge.svg?token=yLu7itEVep)](https://codecov.io/gh/pytesting/test-runner)\n[![License GPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n[![PyPI version](https://badge.fury.io/py/test-runner.svg)](https://badge.fury.io/py/test-runner)\n[![Supported Python Versions](https://img.shields.io/pypi/pyversions/test-runner.svg)](https://github.com/pytesting/test-runner)\n\nRunning Python tests is a complicated task, as it seems that there is not\nstandard way of doing it.\n`test-runner` implements some heuristics that try to run tests with or without\ncoverage measuring, independent of the used testing framework.\n\n## Prerequisites\n\nBefore you begin, ensure you have met the following requirements:\n- You have installed Python at least in version 3.6.\n- You have a recent Linux machine.\n  The library is most likely to not work on another operating system since it is\n  depending on [`benchexec`](https://github.com/sosy-lab/benchexec) for resource\n  handling, which currently only runs on recent versions of Linux.\n- For development it is necessary to have the [`poetry`](https://poetry.eustace.io)\n packaging and dependency management system.\n \n## Installing Test Runner\n\nTest Runner can be easily installed from [PyPI](https://pypi.org) using the\n `pip` utility:\n```bash\npip install test-runner\n```\n\n## Contributing to Test Runner\n\nTo contribute to Test Runner, follow these steps:\n1. Fork this repository.\n2. Setup a virtual environment for development using `poetry`: `poetry install`.\n3. Create a branch: `git checkout -b <branch_name>`.\n4. Make your changes and commit them `git commit -m '<commit_message>'`.\n5. Push to the original branch: `git push origin <project_name>/<location>`.\n6. Create the pull request.\n\nPlease note that we require you to meet the following criteria:\n- Write unit tests for your code.\n- Run linting with `flake8` and `pylint`\n- Run type checking using `mypy`\n- Format your code according to the `black` code style\n\nTo ease the execution of the tools, we provide a `Makefile` with various targets.\nThe easiest way to execute all checks is to run `make check` on a `poetry shell`.\nPush your commits only if they pass all checks!\nThese tools are also executed in continuous integration on TravisCI and will also\n check you pull request.\nFailing a check will block your pull request from being merged!\n\n## Contributors\n\nSee the [Contributors page](https://github.com/pytesting/test-runner/graphs/contributors)\nfor a list of contributors.\nThanks to all contributors!\n\n\n## License\n\n`test-runner` is free software: you can redistribute it and/or modify\nit under the terms of the GNU Lesser General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\n\n`test-runner` is distributed in the hope that it will be useful\nbut WITHOUT ANY WARRANT; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU Lesser General Public License for more details.\n\nYou should have received a [copy](LICENSE.txt) of the\nGNU Lesser General Public License\nalong with `test-runner`.  If not, see\n[https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).\n",
    'author': 'Stephan Lukasczyk',
    'author_email': 'python-test-runner@googlegroups.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pytesting/test-runner',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
