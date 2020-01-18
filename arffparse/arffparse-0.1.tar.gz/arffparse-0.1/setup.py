
from setuptools import setup

with open('README.md', 'r') as fh:
  long_description = fh.read()

setup(
  name='arffparse',
  version='0.1',
  description='Small ARFF parsing tool for datasets',
  long_description=long_description,
  license='MIT',
  url='https://github.com/connormullett/ArffParse',
  author='arff parse',
  author_email='connormullett@gmail.com'
)

