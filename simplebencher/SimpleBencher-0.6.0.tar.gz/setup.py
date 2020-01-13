from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='SimpleBencher',
      version='0.6.0',
      description='Benchmarking Suite',
      author='Christian Schweigel',
      author_email='',
      url='https://github.com/swip3798/Bencher',
      packages=['simple_bencher'],
      long_description = long_description,
      long_description_content_type="text/markdown",
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3 :: Only",
          "Operating System :: OS Independent",
          "Development Status :: 3 - Alpha"
      ]
     )