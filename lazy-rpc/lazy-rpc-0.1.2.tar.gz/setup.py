import setuptools

from lazy_rpc.version import VERSION

def _requires_from_file(filename):
  with open(filename, 'r') as f:
    ret = f.read().splitlines()
    if ret[0].startswith('-i http'):
      del ret[0]
    
    return ret

if __name__ == '__main__':

  extras_require = {
    'dev': _requires_from_file('requirements-dev.txt'),
  }
  
  with open('README.md', 'r') as f:
    long_description = f.read()


  setuptools.setup(
    name='lazy-rpc',
    version=VERSION,
    description='rpc module',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/m0cchi/lazy-rpc',
    packages=setuptools.find_packages(exclude=[
      'test',
      'test.*',
    ]),
    install_requires=_requires_from_file('requirements.txt'),
    extras_require=extras_require,

    license='MIT',
    python_requires='>=3.0',
    classifiers=[
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Operating System :: OS Independent',
    ],

    author='m0cchi',
    author_email='m0cchi@protonmail.com',
  )
