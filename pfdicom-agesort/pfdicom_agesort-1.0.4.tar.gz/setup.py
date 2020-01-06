import sys

# Make sure we are running python3.5+
if 10 * sys.version_info[0]  + sys.version_info[1] < 35:
    sys.exit("Sorry, only Python 3.5+ is supported.")

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
      name             =   'pfdicom_agesort',
      version          =   '1.0.4',
      description      =   'Process ChRIS trees of DICOM data and reorder by age.',
      long_description =   readme(),
      author           =   'FNNDSC',
      author_email     =   'dev@babymri.org',
      url              =   'https://github.com/FNNDSC/pfdicom_agesort',
      packages         =   ['pfdicom_agesort'],
      install_requires =   ['pfdicom'],
      #test_suite       =   'nose.collector',
      #tests_require    =   ['nose'],
      scripts          =   ['bin/pfdicom_agesort'],
      license          =   'MIT',
      zip_safe         =   False
)
