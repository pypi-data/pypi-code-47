#!/usr/bin/env/python3

with open("README.md", "r") as fh:
    long_description = fh.read()

from distutils.core import setup
setup(
  name = 'ProcessedPiRecorder',         
  packages = ['ProcessedPiRecorder'],   
  version = '0.2.0',      
  license='GPLv3',        #https://help.github.com/articles/licensing-a-repository
  description = 'Multiprocessed picamera class for simpler and faster computer vision',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Matthew Davenport',      
  author_email = 'mdavenport@rockefeller.edu', 
  url = 'https://github.com/mattisabrat/ProcessedPiRecorder',
  install_requires=[            # I get to this in a second
          'picamera["array"]==1.13',
          'opencv-contrib-python==3.4.4.19',
          'tifffile==2019.7.26',
          'numpy==1.17.0'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)' ,
    'Programming Language :: Python :: 3 :: Only',
    'Operating System :: POSIX :: Linux'
  ],
)
