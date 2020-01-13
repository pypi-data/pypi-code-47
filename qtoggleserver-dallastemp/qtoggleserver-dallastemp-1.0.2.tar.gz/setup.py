
from setuptools import setup, find_namespace_packages

from qtoggleserver.dallastemp import VERSION


setup(
    name='qtoggleserver-dallastemp',
    version=VERSION,
    description='Dallas DS18B20 temperature sensor support for qToggleServer',
    author='Calin Crisan',
    author_email='ccrisan@gmail.com',
    license='Apache 2.0',

    packages=find_namespace_packages()
)
