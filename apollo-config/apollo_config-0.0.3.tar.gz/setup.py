# encoding: utf-8
"""
apollo 连接工具包


"""
from setuptools import setup, find_packages
import apollo_config

SHORT = u'apollo_config'

setup(
    name='apollo_config',
    version=apollo_config.__version__,
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author=apollo_config.__author__,
    author_email=apollo_config.__email__,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    include_package_data=True,
    package_data={'': ['*.py', '*.pyc']},
    zip_safe=False,
    platforms='any',
    description=SHORT,
    long_description=__doc__,
)
