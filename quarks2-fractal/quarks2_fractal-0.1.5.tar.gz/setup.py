# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['quarks2_fractal',
 'quarks2_fractal.base',
 'quarks2_fractal.classifier',
 'quarks2_fractal.common',
 'quarks2_fractal.datasets',
 'quarks2_fractal.encoders',
 'quarks2_fractal.engine',
 'quarks2_fractal.fpn',
 'quarks2_fractal.linknet',
 'quarks2_fractal.pretrainedmodels',
 'quarks2_fractal.pretrainedmodels.datasets',
 'quarks2_fractal.pretrainedmodels.models',
 'quarks2_fractal.pretrainedmodels.models.resnext_features',
 'quarks2_fractal.pspnet',
 'quarks2_fractal.unet',
 'quarks2_fractal.utils']

package_data = \
{'': ['*'], 'quarks2_fractal.pretrainedmodels.models': ['fbresnet/*']}

install_requires = \
['EasyDict>=1.9,<2.0',
 'albumentations>=0.4.1,<0.5.0',
 'captum>=0.1.0,<0.2.0',
 'click>=7.0,<8.0',
 'efficientnet_pytorch==0.5.1',
 'hyperdash>=0.15.3,<0.16.0',
 'ipykernel>=5.1,<6.0',
 'ipython>=7.8,<8.0',
 'loguru>=0.3.2,<0.4.0',
 'opencv-python>=4.1,<5.0',
 'pandas>=0.25.2,<0.26.0',
 'pretrainedmodels>=0.7.4,<0.8.0',
 'scikit-learn>=0.21.3,<0.22.0',
 'torch==1.3.0',
 'torchnet>=0.0.4,<0.0.5',
 'torchvision==0.4.1']

entry_points = \
{'console_scripts': ['batched_inference = '
                     'quarks2_fractal.utils.batched_inference:batched_inference',
                     'f1_score = quarks2_fractal.utils.f1_score:f1_score',
                     'infer_img = quarks2_fractal.engine.infer:infer_img_click',
                     'infer_video = '
                     'quarks2_fractal.engine.infer:infer_video_click',
                     'train = quarks2_fractal.engine.trainer:main']}

setup_kwargs = {
    'name': 'quarks2-fractal',
    'version': '0.1.5',
    'description': 'Integrated image classification and semantic segmentation package',
    'long_description': None,
    'author': 'PrakashJay',
    'author_email': 'vanapalli.prakash@fractal.ai',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '==3.6.9',
}


setup(**setup_kwargs)
