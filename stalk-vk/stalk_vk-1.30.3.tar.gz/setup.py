import stalk

from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='stalk_vk',
    url='https://github.com/Adonai-ai',
    author='Adonai-ai',
    author_email='vlad.gremchuk@mail.ru',
    license='MIT',
    version=stalk.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    entry_points={
        'console_scripts':['stalk_vk = stalk.core:main']
    },
    install_requires=[
        'Flask','vk_api','bs4'
    ],
)
