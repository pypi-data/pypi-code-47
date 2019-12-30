# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['video_utils']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.0,<0.5.0',
 'ffmpy>=0.2.2,<0.3.0',
 'pymediainfo>=4.1,<5.0',
 'tqdm>=4.40.2,<5.0.0']

setup_kwargs = {
    'name': 'video-utils',
    'version': '2.0.1',
    'description': 'This library is used for lots of shared functionality around parsing TV shows and movies',
    'long_description': None,
    'author': 'Justin Dray',
    'author_email': 'justin@dray.be',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
