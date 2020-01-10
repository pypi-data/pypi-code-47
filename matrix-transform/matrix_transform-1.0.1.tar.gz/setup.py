# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['matrix_transform']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.13', 'scipy>=0.17']

setup_kwargs = {
    'name': 'matrix-transform',
    'version': '1.0.1',
    'description': 'scikit-image geometric transform module, no extra shit',
    'long_description': '# matrix_transform\n\nscikit-image geometric transform module, no extra shit\n',
    'author': 'm.shlyamov',
    'author_email': 'm.shlyamov@yandex.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SandLabs/matrix_transform',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5',
}


setup(**setup_kwargs)
