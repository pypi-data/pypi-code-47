from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='cp-redis',
      version=version,
      description="This is Carpool Project subpackage: cp cp-redis",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='petergra',
      author_email='lvpet@esquel.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'redis',
            'Django',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
