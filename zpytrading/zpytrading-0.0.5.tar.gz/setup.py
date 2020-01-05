from distutils.core import setup

with open("README.txt", "r") as fh:
    long_description = fh.read()

setup(
  name = 'zpytrading',
  packages = ['zpytrading'],
  version = '0.0.5',
  license='MIT',
  description = 'Zinnion Streaming / Trading SDK',
  long_description=long_description,
  long_description_content_type="text/markdown",  
  author = 'Mauro Delazeri',
  author_email = 'mauro@zinnion.com',
  url = 'https://github.com/Zinnion/zpytrading',
  download_url = 'https://github.com/Zinnion/zpytrading/archive/v0.0.5.tar.gz',
  keywords = ['zpytrading','zinnion','sdk','api'],
  install_requires=[
          'pyzmq',
      ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],  
)
