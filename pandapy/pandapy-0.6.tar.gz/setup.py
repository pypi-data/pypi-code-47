from setuptools import setup, Command
import os
import sys

class CleanCommand(Command):
    user_options = []
    def initialize_options(self):
        self.cwd = None
    def finalize_options(self):
        self.cwd = os.getcwd()
    def run(self):
        assert os.getcwd() == self.cwd, 'Must be in package root: %s' % self.cwd
        os.system ('rm -rf build dist *.pyc *.tgz *.egg-info')

setup(name='pandapy',
      version='0.6',
      description='Structured Numpy with Pandas a Click Away',
      url='https://github.com/firmai/pandapy',
      author='snowde',
      author_email='d.snow@firmai.org',
      license='MIT',
      packages=['pandapy'],
      install_requires=[
          'pandas',
          'numpy',
          'scipy',
          'operator',
          'itertools',
          'numpy-groupies'

      ],
      zip_safe=False)
