#!/usr/bin/env python
# coding=utf-8
"""Setup script for blacksap project"""

from setuptools import setup

setup(name='blacksap',
      version='1.7',
      description='Track torrent RSS feeds',
      author='Jesse Almanrode',
      author_email='jesse@almanrode.com',
      url='https://bitbucket.org/isaiah1112/blacksap',
      py_modules=['blacksap'],
      license='GNU General Public License v3 or later (GPLv3+)',
      install_requires=['click==7.0',
                        'colorama==0.4.3',
                        'feedparser==5.2.1',
                        'PySocks==1.7.1',
                        'requests==2.22.0',
                        ],
      platforms=['Linux',
                 'Darwin',
                 ],
      entry_points="""
            [console_scripts]
            blacksap=blacksap:cli
      """,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Natural Language :: English',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Communications :: File Sharing',
          'Topic :: Utilities',
          ],
      )
