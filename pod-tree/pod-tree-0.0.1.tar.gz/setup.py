

#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='pod-tree',
    version='0.0.1',
    author='gujitao',
    author_email='taojigu@163.com',
    url='https://zhuanlan.zhihu.com/p/26159930',
    description=u'tool for extracting dependency from  Podfile.lock',
    packages=['pod_tree'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pill=pod_tree.__init__:pill',
            #'pill=pod-tree._init_:pill'
        ]
    }
)