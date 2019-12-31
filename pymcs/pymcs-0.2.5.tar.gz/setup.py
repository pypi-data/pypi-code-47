#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['pymcs']

package_data = \
{'': ['*']}

install_requires = \
['pandas >=0.25', 'tqdm >=4.41', 'cx_Oracle >= 7.3']

setup(name='pymcs',
      version='0.2.5',
      description='Top-level package for pymcs.',
      author='K.-Michael Aye',
      author_email='kmichael.aye@gmail.com',
      url='https://github.com/michaelaye/pymcs',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      python_requires='~=3.7',
     )
