from setuptools import setup, find_packages
from curv_amqp import __version__
from pathlib import Path

setup(name='curv_amqp',
      long_description=Path(__file__).parent.joinpath("README.md").read_text(),
      long_description_content_type="text/markdown",
      license="MIT",
      url='http://github.com/rep-ai/curv_amqp',
      version=__version__,
      packages=find_packages(),
      install_requires=['pika', 'simplejson', 'dataclasses'])
