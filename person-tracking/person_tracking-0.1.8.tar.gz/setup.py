# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['person_tracking',
 'person_tracking.fractal.anchors',
 'person_tracking.fractal.common_utils',
 'person_tracking.fractal.deep_sort',
 'person_tracking.fractal.loaders',
 'person_tracking.fractal.losses',
 'person_tracking.fractal.metrics',
 'person_tracking.fractal.nets',
 'person_tracking.fractal.optims',
 'person_tracking.fractal.superai',
 'person_tracking.fractal.superai.Nets',
 'person_tracking.fractal.superai.Nets.resnext_features',
 'person_tracking.fractal.vis_lib']

package_data = \
{'': ['*'],
 'person_tracking': ['cfgs/*', 'data/coco/*'],
 'person_tracking.fractal.superai': ['.ipynb_checkpoints/*']}

install_requires = \
['PILLOW>=7.0,<8.0',
 'matplotlib>=3.1,<4.0',
 'opencv-python>=4.1,<5.0',
 'progressbar>=2.5,<3.0',
 'scipy>=1.4,<2.0',
 'sklearn>=0.0.0,<0.0.1',
 'torch>=1.3,<2.0',
 'torchvision>=0.5.0,<0.6.0']

setup_kwargs = {
    'name': 'person-tracking',
    'version': '0.1.8',
    'description': 'person tracking',
    'long_description': None,
    'author': 'Sindhura',
    'author_email': 'sindhura.k@fractal.ai',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.6.9',
}


setup(**setup_kwargs)
