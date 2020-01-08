"""Setup sony_bravia_psk package."""
from setuptools import setup, find_packages

setup(
    name='nanSonyTV',
    version='0.0.1',
    description='Library for Sony Bravia TVs with Pre-Shared Key option',
    url='https://github.com/aaronj-nzme/Sony_TV',
    maintainer='Nan',
    maintainer_email='499521010@qq.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests'],
    keywords='Sony Bravia TV PSK for Home Assistant',
    include_package_data=True,
    zip_safe=False
)
