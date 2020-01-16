from distutils.core import setup

setup(
  name = 'InfiniteTrends',
  packages = ['InfiniteTrends'],
  version = '0.2',
  license='MIT',
  description = 'An upgraded Google Trends API that can query infinitely many terms.',
  author = 'Asher Noel',
  author_email = 'asher13a@gmail.com',
  url = 'https://www.ashernoel.io',
  download_url = 'https://github.com/ashernoel/InfiniteTrends/archive/v_02.tar.gz',
  keywords = ['Google Trends', 'Interest', 'Viral', 'Related'],
  install_requires=[
          'pytrends',
          'pandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
  ],
)
