# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arus',
 'arus.core',
 'arus.core.accelerometer',
 'arus.core.accelerometer.features',
 'arus.core.accelerometer.features.tests',
 'arus.core.accelerometer.tests',
 'arus.core.annotation',
 'arus.core.annotation.tests',
 'arus.core.libs',
 'arus.core.libs.dsp',
 'arus.core.libs.dsp.tests',
 'arus.core.libs.mhealth_format',
 'arus.core.libs.mhealth_format.tests',
 'arus.core.stream',
 'arus.core.stream.tests',
 'arus.core.tests',
 'arus.models',
 'arus.models.tests',
 'arus.plugins',
 'arus.plugins.metawear']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.1,<4.0',
 'numpy>=1.17,<2.0',
 'pandas>=0.25.1,<0.26.0',
 'pathos>=0.2.5,<0.3.0',
 'pymetawear>=0.12.0,<0.13.0',
 'pysimplegui>=4.13.0,<5.0.0',
 'scikit-learn>=0.22,<0.23',
 'scipy>=1.3,<2.0',
 'seaborn>=0.9.0,<0.10.0']

setup_kwargs = {
    'name': 'arus',
    'version': '0.6.0',
    'description': 'Activity Recognition with Ubiquitous Sensing',
    'long_description': '# `arus` package\n\n\n\n__arus__ python package provides a computation framework to manage and process ubiquitous sensory data for activity recognition.\n\n[![PyPI version](https://badge.fury.io/py/arus.svg)](https://badge.fury.io/py/arus)\n[![Downloads](https://pepy.tech/badge/arus)](https://pepy.tech/project/arus)\n[![Build Status](https://github.com/qutang/arus/workflows/Continuous%20integration/badge.svg)](https://github.com/qutang/arus/actions)\n[![codecov](https://codecov.io/gh/qutang/arus/branch/master/graph/badge.svg)](https://codecov.io/gh/qutang/arus)\n\n\n## Prerequists\n\n```bash\npython >= 3.6\n```\n\n### Windows\n\nFor `arus[metawear]` extra, you need,\n\n```bash\nVisual Studio C++ SDK (v14.1)\nWindows SDK (10.0.16299.0)\nWindows SDK (10.0.17763.0)\n```\n\n### Ubuntu\n\nFor `arus[metawear]` extra, you need,\n\n```bash\nlibbluetooth-dev\nlibboost-all-dev\nbluez\n```\n\n## Installation\n\n```bash\n> pip install arus\n```\n\nor with `pipenv`\n\n```bash\n> pipenv install arus\n```\n\nor with `poetry`\n\n```bash\n> poetry add arus\n```\n\n## Extras\n\n`arus[metawear]`: In addition to the core functionality, this extra provides support for metawear devices.\n\n## For developer\n\n### Prerequists\n\n```bash\npython >= 3.6\npoetry >= 0.12.17\n```\n\n### Set up development environment\n\n```bash\n> git clone https://github.com/qutang/arus.git\n> cd arus\n> poetry install\n```',
    'author': 'qutang',
    'author_email': 'tqshelly@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/qutang/arus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
