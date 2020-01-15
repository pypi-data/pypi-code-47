import ast
import io
import os
import re

from setuptools import setup, find_packages


def read(*names, **kwargs):
    return io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


def version(filename):
    """Return version string."""
    with open(filename) as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s

requires = ['requests']

setup(name='totango-divvy',
      version=version(os.path.join('totango', '__init__.py')),
      description='Totango Python Library for DivvyHQ',
      long_description='%s\n%s' % (read('README.rst'), re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))),
      author='DivvyHQ',
      author_email='contact@divvyhq.com',
      url='http://github.com/DivvyHQ/totango-python',
      license='Apache 2.0',
      packages=find_packages(),
      zip_safe=False,
      classifiers=[
          # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords=[
        'totango api', 'totango python'
      ],
      install_requires = requires,
)
