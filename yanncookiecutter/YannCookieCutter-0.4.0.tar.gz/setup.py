import os
import codecs
from setuptools import setup
from setuptools.config import read_configuration


conf_pth = os.path.join(os.path.dirname(os.path.abspath(__file__)),'setup.cfg')
conf_dict = read_configuration(conf_pth)

opt = conf_dict['options']
if not 'install_requires' in opt.keys():
    opt['install_requires'] = []

with codecs.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'requirements.txt'),mode='r', encoding='utf-8') as f:
    req = f.read().strip().split('\n')
    conf_dict['options']['install_requires'].extend(req)

setup(**conf_dict['option'],**conf_dict['metadata'])

