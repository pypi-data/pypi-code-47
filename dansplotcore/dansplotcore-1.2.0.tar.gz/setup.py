import os
from setuptools import setup

with open(os.path.join('..', 'README.md')) as f: readme = f.read()

setup(
    name='dansplotcore',
    version='1.2.0',
    description='speedy interactive plots',
    long_description=readme,
    url='http://github.com/dansgithubuser/dansplotcore',
    author='danspypiuser',
    author_email='dansonlinepresence@gmail.com',
    license='MIT',
    packages=['dansplotcore'],
    install_requires=['danssfmlpy==1.2.0'],
    zip_safe=False,
)
