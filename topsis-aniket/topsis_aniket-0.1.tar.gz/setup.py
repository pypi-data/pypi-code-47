from distutils.core import setup
setup(
  name = 'topsis_aniket',
  packages = ['topsis_aniket'],
  version = '0.1',
  license='MIT',
  description = 'A muliti-criteria decision analysis method.',
  author = 'Aniket Gupta',
  author_email = 'aniketgupta1495@gmail.com',
  url = 'https://github.com/aniket1402/topsis_aniket.git',
  download_url = 'https://github.com/aniket1402/topsis_aniket/archive/v_01.tar.gz',
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],
  install_requires=[
          'numpy',
          'pandas',
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
  ],
)
