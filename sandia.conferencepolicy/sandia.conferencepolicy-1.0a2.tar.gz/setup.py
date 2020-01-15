# -*- coding: utf-8 -*-
"""Installer for the sandia.conferencepolicy package."""

from setuptools import setup, find_packages
import os


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])

setup(name='sandia.conferencepolicy',
      version='1.0a2',
      description="Policy product for Sandia multiconference website",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: Addon",
          "Framework :: Plone :: 5.2",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Operating System :: OS Independent",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
      ],
      keywords='Python Plone',
      author='T. Kim Nguyen',
      author_email='nguyen@plone.org',
      url='https://bitbucket.org/sixfeetup/sandia.conferencepolicy',
      project_urls={
          'PyPI': 'https://pypi.python.org/pypi/sandia.conferencepolicy',
          'Source': 'https://bitbucket.org/sixfeetup/sandia.conferencepolicy',
      },
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sandia'],
      include_package_data=True,
      zip_safe=False,
      python_requires="==2.7, >=3.6",
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'z3c.jbot',
          'plone.api>=1.8.4',
          'plone.restapi',
          'plone.app.dexterity',
          'collective.easyform',
          'plone.app.mosaic',
          'sandia.conferencetheme',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              # Plone KGS does not use this version, because it would break
              # Remove if your package shall be part of coredev.
              # plone_coredev tests as of 2016-04-01.
              'plone.testing>=5.0.0',
              'plone.app.contenttypes',
              'plone.app.robotframework[debug]',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      [console_scripts]
      update_locale = sandia.conferencepolicy.locales.update:update_locale
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
