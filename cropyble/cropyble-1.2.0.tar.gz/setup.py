import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / 'README.md').read_text()

setup(
  name = 'cropyble',
  packages = ['cropyble'],
  version = '1.2.0',
  license='MIT',
  long_description=README,
  long_description_content_type='text/markdown',
  description = 'Cropyble is a module that allows a user to easily perform crops on an image containing recognizable text. This module utilizes optical character recognition (OCR) from Google by way of pytesseract.',
  author = 'Skyler Burger',
  author_email = 'skylerburger@gmail.com',
  url = 'https://github.com/SkylerBurger/cropyble',
  download_url = 'https://github.com/SkylerBurger/cropyble/archive/1.2.1.tar.gz',
  keywords = ['OCR', 'tesseract', 'pytesseract', 'crop', 'character recognition'],
  install_requires=[
          'pytesseract',
          'pillow',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)
