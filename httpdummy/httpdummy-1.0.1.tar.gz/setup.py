from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='httpdummy',
      version='1.0.1',
      description='A dummy http server that prints requests and responds',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/ksofa2/httpdummy',
      author='Kris Steinhoff',
      author_email='ksteinhoff@gmail.com',
      license='Apache 2.0',
      packages=['httpdummy'],
      install_requires=[
          'colorama ~= 0.4',
          'PyYAML ~= 5.3',
          'watchdog ~= 0.9',
          'Werkzeug ~= 0.16',
      ],
      entry_points={
          'console_scripts': ['httpdummy=httpdummy.server:main'],
      },
      zip_safe=False)
