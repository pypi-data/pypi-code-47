# pylint: skip-file
from setuptools import setup, find_packages

setup(name='gdalhelpers',
      version='0.1.7',
      description='GDAL helpers, checks, classes and functions package',
      url='https://github.com/JanCaha/gdalhelpers',
      author='Jan Caha',
      author_email='jan.caha@outlook.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'markdown',
          'gdal',
          'numpy',
          'angles',
          'nose'
      ],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose']
      )
