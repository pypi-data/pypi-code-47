# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mebula']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=1.7.11,<2.0.0', 'oci>=2.9.0,<3.0.0']

setup_kwargs = {
    'name': 'mebula',
    'version': '0.1.2',
    'description': '',
    'long_description': 'Mebula\n======\n\nMebula is a framework which you can use in your testing code to mock your calls to cloud providers\' APIs.\nAt the moment, Oracle\'s OCI and Google Cloud is supported.\n\nUsage\n-----\n\nYou can use the ``mock_google`` context manager and then use the Googe API functions as normal:\n\n.. code:: python\n\n    import googleapiclient.discovery\n    import pytest\n\n    from mebula import mock_google\n\n    @pytest.fixture(scope="function")\n    def client():\n        with mock_google():\n            yield googleapiclient.discovery.build("compute", "v1")\n\n    def my_test(client):\n        assert client.instances().list(project="foo", zone="bar").execute() == {}\n\nCoverage\n--------\n\nCoverage is very minimal at the moment. Only launching and listing instances is supported.\n',
    'author': 'Matt Williams',
    'author_email': 'matt@milliams.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/milliams/mebula',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
