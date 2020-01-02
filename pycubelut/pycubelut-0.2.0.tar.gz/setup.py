# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pycubelut']
install_requires = \
['colour-science>=0.3.14,<0.4.0',
 'numpy==1.17.3',
 'pillow>=6.2.1,<7.0.0',
 'scipy>=1.4.1,<2.0.0']

entry_points = \
{'console_scripts': ['cubelut = pycubelut:main']}

setup_kwargs = {
    'name': 'pycubelut',
    'version': '0.2.0',
    'description': 'Tool for Applying Adobe Cube LUTs to Images',
    'long_description': None,
    'author': 'Yoonsik Park',
    'author_email': 'park.yoonsik@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
