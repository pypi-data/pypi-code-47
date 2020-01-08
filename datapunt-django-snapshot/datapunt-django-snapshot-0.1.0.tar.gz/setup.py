from setuptools import setup, find_packages

import snapshot

setup(
    name="datapunt-django-snapshot",
    version=snapshot.__version__,
    license='Mozilla Public License 2.0',

    author='Datapunt Amsterdam',
    author_email='datapunt@amsterdam.nl',

    packages=find_packages(),
    description='A collection of classes to easily scrape/import APIs',
    install_requires=['requests', 'django']
)
