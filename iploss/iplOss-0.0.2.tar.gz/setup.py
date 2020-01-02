import setuptools
from setuptools import setup

setup(
    name='iplOss',  # 应用名
    version='0.0.2',  # 版本号
    description='iPayLinks FileServer tool',
    packages=['iplOss'],  # 包括在安装包内的 Python 包
    install_requires=['oss2']
    # packages=setuptools.find_packages(exclude=['test', 'examples', 'script', 'tutorials']),  # 包内需要引用的文件夹
)
