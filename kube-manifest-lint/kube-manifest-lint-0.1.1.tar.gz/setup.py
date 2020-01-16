# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kube_manifest_lint']

package_data = \
{'': ['*'], 'kube_manifest_lint': ['schemas/v1.17.0/*']}

install_requires = \
['PyYAML>=5.3,<6.0', 'jsonschema>=3.2.0,<4.0.0']

entry_points = \
{'console_scripts': ['kube-manifest-lint = kube_manifest_lint:main.main']}

setup_kwargs = {
    'name': 'kube-manifest-lint',
    'version': '0.1.1',
    'description': 'Kubernetes manifest linter using JSON Schema',
    'long_description': None,
    'author': 'Henning Jacobs',
    'author_email': 'henning@jacobs1.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
