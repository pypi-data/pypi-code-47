from distutils.core import setup, Extension

pydinemic = Extension('pydinemic',
                      sources=['src/pydinemic/module.cpp',
                               'src/pydinemic/pyaction.cpp',
                               'src/pydinemic/pydmodel.cpp'],
                      include_dirs=['/usr/include'],
                      library_dirs=['/usr/lib/x86_64-linux-gnu/'],
                      runtime_library_dirs=['/usr/lib/x86_64-linux-gnu/'],
                      libraries=['boost_python3', 'dinemic'])

setup(name='pydinemic',
      version='20.01',
      description='Dinemic framework for python',
      package_dir={'': 'src'},
      packages=['pkg'],
      ext_modules=[pydinemic])
