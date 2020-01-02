from distutils.core import setup, Extension
from Cython.Build import cythonize


ext_modules = [ 
    Extension('pynfftls',
               libraries = ['m','nfft3','fftw3'],
               depends  = ['io.h', 'ls.h','nfft.h', 'utils.h'],
               sources = ['pynfftls.pyx','nfft.c','ls.c','utils.c'])
##               extra_compile_args = ['-finline-functions','-fstrict-aliasing','-malign-double','-std=c99'])
    ]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name = 'pynfftls',
      version = '1.5',
      description = "Fast Lomb-Scargle periodogram using Non-equispaced Fast Fourier Transform (NFFT)  by B. Leroy",
      author = 'B. Leroy - Python interface by R. Samadi',
      author_email = 'reza.samadi@obspm.fr',
      url =  'http://lesia.obspm.fr/',
      long_description = long_description,
      long_description_content_type= 'text/markdown',
      ext_modules =   cythonize(ext_modules)
      )
