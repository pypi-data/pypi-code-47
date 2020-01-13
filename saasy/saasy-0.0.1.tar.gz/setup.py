from setuptools import setup, find_packages
from saasy import __version__


setup(name='saasy',
      version=__version__,
      description='Saasy API Client',
      url='https://github.com/pixelpassion/saasy',
      author='Jens Neuhaus',
      author_email='hello@pixelpassion.io',
      maintainer='Jens Neuhaus',
      maintainer_email='hello@pixelpassion.io',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[  # I get to this in a second
          'requests',
      ],
      )
