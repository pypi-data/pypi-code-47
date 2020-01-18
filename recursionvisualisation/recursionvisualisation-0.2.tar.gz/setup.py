from distutils.core import setup
setup(
  name = 'recursionvisualisation',
  packages = ['recursionvisualisation'],
  version = '0.2',
  license='MIT',
  description = 'A module to help visualise recursion tree for various recursion functions.',
  author = 'Puneeth K',
  author_email = 'puneethk.cs17@bmsce.ac.in',
  url = 'https://github.com/punndcoder28/Recursion-Visualization',
  download_url = 'https://github.com/punndcoder28/Recursion-Visualization/archive/v_02.tar.gz',
  keywords = ['Python 3.6', 'Recursion', 'Recursion Visualisation'],
  install_requires=[
          'graphviz',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)