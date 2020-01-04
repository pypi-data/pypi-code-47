# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tft', 'tft.phoebe']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.8.1,<5.0.0',
 'lxml>=4.4.2,<5.0.0',
 'prometheus-client>=0.7.1,<0.8.0',
 'requests',
 'ruamel.yaml>=0.15.51,<0.16.0']

entry_points = \
{'console_scripts': ['phoebe-jenkins = tft.phoebe.exporter_jenkins:main',
                     'phoebe-openstack = tft.phoebe.exporter_openstack:main']}

setup_kwargs = {
    'name': 'tft-phoebe',
    'version': '0.0.1',
    'description': 'Data gathering proxy for Prometheus toolkit',
    'long_description': "= Phoebe\n\nPhoebe is a data gathering proxy for https://prometheus.io/[Prometheus] toolkit. Its goal is to gather metrics from systems that don't provide their own native Prometheus export, and make them available for digestion by Prometheus.\n\n\n== How to run an exporter\n\n[source,shell]\n....\n$ poetry install\n$ poetry run phoebe-openstack --config=<your config file> --export=<filepath or - for stdout>\n....\n\nOr, without using Poetry at all, using PyPI package:\n\n[source,shell]\n....\n$ pip install ... # as soon as we publish it, I 'm going to fix the package name\n$ phoebe-openstack --config=<your config file> --export=<filepath or - for stdout>\n....\n",
    'author': 'Jakub Haruda',
    'author_email': 'jharuda@redhat.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/phoebe',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
