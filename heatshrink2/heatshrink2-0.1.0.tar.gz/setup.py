from os import path
from codecs import open
from setuptools import setup, Extension

try:
    from Cython.Build import cythonize
except ImportError:
    USE_CYTHON = False
else:
    USE_CYTHON = True


# Compiled file extension to use. If we're not using Cython,
# just use the plain C file.
EXT = '.pyx' if USE_CYTHON else '.c'

heatshrink_module = Extension('heatshrink2.core',
                              include_dirs=['.', './heatshrink2/_heatshrink'],
                              extra_compile_args=['-std=c99'],
                              sources=['heatshrink2/core' + EXT,
                                       'heatshrink2/_heatshrink/heatshrink_encoder.c',
                                       'heatshrink2/_heatshrink/heatshrink_decoder.c'])

if USE_CYTHON:
    extensions = cythonize([heatshrink_module])
else:
    extensions = [heatshrink_module]

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='heatshrink2',
      version='0.1.0',
      # Author details
      author='Antonis Kalou @ JOHAN Sports, Erik Moqvist',
      author_email='antonis@johan-sports.com, erik.moqvist@gmail.com',
      # Project details
      description='Python bindings to the heatshrink library',
      long_description=long_description,
      url='https://github.com/eerimoq/pyheatshrink',
      license='ISC',
      classifiers=[
          'Programming Language :: Python :: 3'
      ],
      keywords='compression binding heatshrink LZSS',
      test_suite='tests',
      packages=['heatshrink2'],
      ext_modules=extensions)
