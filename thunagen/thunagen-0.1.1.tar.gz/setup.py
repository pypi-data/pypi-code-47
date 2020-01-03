# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['thunagen']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=7.0.0,<8.0.0',
 'google-cloud-storage>=1.24.1,<2.0.0',
 'lazy_object_proxy>=1.4.3,<2.0.0',
 'logbook>=1.5.3,<2.0.0',
 'python-dotenv>=0.10.3,<0.11.0']

setup_kwargs = {
    'name': 'thunagen',
    'version': '0.1.1',
    'description': 'Google Cloud function to generate thumbnail for images in Google Storage.',
    'long_description': '========\nThunagen\n========\n\n\nGoogle Cloud function to generate thumbnail for images in Google Storage.\n\nConvention\n----------\n\nThe thumbnails are placed in a folder "thumbnails" at the same place as original file.\n\nThe thumbnail size is appended to filename, right before the extention part. For example:\n\n\n.. code-block::\n\n    bucket\n    └── folder\n        ├── photo.jpg\n        └── thumbnails\n            ├── photo_128x128.jpg\n            └── photo_512x512.jpg\n\nThe function expect these environment variables to be set:\n\n- ``THUMB_SIZES``: Size of thumbnail to be generated. Example: ``512x512,128x128``.\n\n- ``MONITORED_PATHS``: Folders (and theirs children) where the function will process the uploaded images. Muliple paths are separated by ":", like ``user-docs:user-profiles``.\n\nThe variables can be passed via *.env* file in the working directory.\n\nInclude to your project\n-----------------------\n\nThunagen is provided without a *main.py* file, for you to easier incorporate to your project, where you may have your own way to configure deployment environment (different bucket for "staging" and "production", for example).\n\nTo include Thunagen, from your *main.py*, do:\n\n.. code-block:: py\n\n    from thunagen.functions import generate_gs_thumbnail\n',
    'author': 'Nguyễn Hồng Quân',
    'author_email': 'ng.hong.quan@gmail.com',
    'maintainer': 'Nguyễn Hồng Quân',
    'maintainer_email': 'ng.hong.quan@gmail.com',
    'url': 'https://github.com/sunshine-tech/thunagen.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
