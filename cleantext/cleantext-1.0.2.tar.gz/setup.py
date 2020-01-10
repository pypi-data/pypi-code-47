import os
from setuptools import setup


rootdir = os.path.abspath(os.path.dirname(__file__))
setup(
   name='cleantext',
   version='1.0.2',
   description='A package to clean the raw text',
   
   author='Prasanth Gudiwada',
   author_email='prasanth.gudiwada@gmail.com',
   url='https://github.com/prasanthg3/cleantext',
   license='MIT',
   long_description = open(os.path.join(rootdir, 'README.md')).read(),
   long_description_content_type='text/markdown',
   packages=['cleantext'],  
   install_requires=['nltk'],
)