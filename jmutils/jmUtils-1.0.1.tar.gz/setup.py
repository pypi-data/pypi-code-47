# coding=UTF-8
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
try:
    with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''

setup(
    # Ver PEP 426 (name)
    # Iniciar ou terminar com letra ou número
    name='jmUtils',

    # Ver PEP 440
    # O formato pode ser assim:

    # 1.2.0.dev1  # Development release
    # 1.2.0a1     Alpha Release
    # 1.2.0b1     Beta Release
    # 1.2.0rc1    Release Candidate
    # 1.2.0       Final Release
    # 1.2.0.post1 Post Release
    # 15.10       Date based release
    # 23          Serial release

    version='1.0.1',
    
    description='Minhas Utilidades',
    long_description=long_description,

    # A página do projeto
    url='https://github.com/jorgemartins72/jmUtils',

    # Detalhes do Autor
    author=u'Jorge Martins',
    author_email='jorgemartins72@gmail.com',

    # Choose your license
    license='MIT',
    
    packages=['jmutils'],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers

    # What does your project relate to?
    # keywords='exemplo tutorial desenvolvimento',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # install_requires=['sh>=1.11'],

)
