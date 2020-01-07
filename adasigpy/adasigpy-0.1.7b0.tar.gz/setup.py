# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['adasigpy', 'adasigpy.domain', 'adasigpy.interface']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.17.4,<2.0.0', 'scipy>=1.4.0,<2.0.0', 'stft>=0.5.2,<0.6.0']

setup_kwargs = {
    'name': 'adasigpy',
    'version': '0.1.7b0',
    'description': 'Adaptive Signal Processing Package in Python',
    'long_description': None,
    'author': 'borley1211',
    'author_email': 'km.isetan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
