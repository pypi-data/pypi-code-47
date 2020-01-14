from setuptools import setup

setup(
  name = 'reformer-pytorch',
  packages = ['reformer-pytorch'],
  version = '0.1',
  license='MIT',
  description = 'Reformer, the Efficient Transformer, Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/reformer-pytorch',
  download_url = 'https://github.com/lucidrains/reformer-pytorch/archive/v_01.tar.gz',
  keywords = ['transformers', 'attention', 'artificial intelligence'],
  install_requires=[
      'revtorch',
      'torch',
  ],
  classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6',
  ],
)