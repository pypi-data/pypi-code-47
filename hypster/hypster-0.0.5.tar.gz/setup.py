# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hypster',
 'hypster.estimators',
 'hypster.estimators.classification',
 'hypster.estimators.regression']

package_data = \
{'': ['*'], 'hypster.estimators': ['classification/.ipynb_checkpoints/*']}

install_requires = \
['category_encoders>=2.1.0,<3.0.0',
 'lightgbm>=2.3.1,<3.0.0',
 'numpy>=1.18.0,<2.0.0',
 'optuna>=0.19.0,<0.20.0',
 'pandas>=0.25.3,<0.26.0',
 'scikit-learn>=0.22,<0.23',
 'scipy>=1.4.1,<2.0.0',
 'xgboost>=0.90,<0.91']

setup_kwargs = {
    'name': 'hypster',
    'version': '0.0.5',
    'description': 'HyPSTER is a brand new Python package that helps you find compact and accurate ML Pipelines while staying light and efficient',
    'long_description': None,
    'author': 'Gilad Rubin',
    'author_email': 'gilad.rubin@gmail.com',
    'maintainer': 'Tal Peretz',
    'maintainer_email': None,
    'url': 'https://github.com/gilad-rubin/hypster',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5.7,<=3.8',
}


setup(**setup_kwargs)
