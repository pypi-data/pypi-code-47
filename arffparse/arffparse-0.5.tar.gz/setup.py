
from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
  long_description = fh.read()

setup(
  name='arffparse',
  version='0.5',
  description='Small ARFF parsing tool for datasets',
  long_description=long_description,
  license='MIT',
  url='https://github.com/connormullett/ArffParse',
  author='arff parse',
  author_email='connormullett@gmail.com',
  packages=find_packages(),
  entry_points={
    'console_scripts': [
      'arffparse=src.arffparse:main'
    ]
  }
)

