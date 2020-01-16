from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'InfiniteTrends',
  packages = ['InfiniteTrends'],
  version = '0.3',
  license='MIT',
  description = 'An upgraded Google Trends API that can query infinitely many terms.',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Asher Noel',
  author_email = 'asher13a@gmail.com',
  url = 'https://www.ashernoel.io',
  download_url = 'https://github.com/ashernoel/InfiniteTrends/archive/v_03.tar.gz',
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
