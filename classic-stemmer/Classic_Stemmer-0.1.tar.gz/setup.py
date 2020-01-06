# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 11:22:45 2020

@author: Abhilash
"""


from distutils.core import setup
setup(
  name = 'Classic_Stemmer',         
  packages = ['Classic_Stemmer'],   
  version = '0.1',       
  license='MIT',        
  description = 'Implementation of Porter Stemmer algorithm (M.F Porter 1980)',   
  author = 'ABHILASH MAJUMDER',
  author_email = 'abhilash.majumder@hsbc.co.in',
  url = 'https://github.com/abhilash1910/Classic_Stemmer',   
  download_url = 'https://github.com/abhilash1910/Classic_Stemmer/archive/v_01.tar.gz',    
  keywords = ['stemmer', 'porter', 'porter stemmer','stemming','string','linguistics','computational'],   
  install_requires=[           

          'numpy',         
          'pandas' 
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
     'Programming Language :: Python :: 2.5',      
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)

