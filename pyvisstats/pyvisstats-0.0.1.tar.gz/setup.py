import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    sys.exit('Sorry, Python < 3.6 is not supported')

REQUIRED_PACKAGES = ['matplotlib',
                     'numpy',
                     'pandas',
                     'scipy',
                     'scikit-posthocs',
                     'seaborn']

with open("README.rst", "r") as f:
    long_description = f.read()

setup(name='pyvisstats',
      version='0.0.1',
      description='Python package for computing and visualizing statistics.',
      url='https://github.com/ad12/pyvisstats',
      author='Arjun Desai',
      author_email='arjundd@stanford.edu',
      packages=find_packages(),
      install_requires=REQUIRED_PACKAGES,
      classifiers=[
          "Programming Language :: Python :: 3",
          "Operating System :: OS Independent",
      ],
      license='MIT'
)
