# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['jrpytensorflow', 'jrpytensorflow.datasets']

package_data = \
{'': ['*'],
 'jrpytensorflow': ['vignettes/*'],
 'jrpytensorflow.datasets': ['data/*']}

install_requires = \
['h5py>=2.10,<3.0',
 'pip>=19,<20',
 'pyyaml>=5.3,<6.0',
 'scikit-learn>=0.22,<0.23',
 'tensorboard>=2.1,<3.0',
 'tensorflow-datasets>=1.3,<2.0',
 'tensorflow==2.1.0rc1']

setup_kwargs = {
    'name': 'jrpytensorflow',
    'version': '0.1.5',
    'description': '',
    'long_description': None,
    'author': 'Jamie',
    'author_email': 'jamie@jumpingrivers.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
