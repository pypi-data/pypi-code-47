#!/usr/bin/env python

from distutils.core import setup


setup(name = 'rubix_cube',
	  packages = ['rubix_cube'],   
	  version = '0.1.1',	
	  license='MIT',  
	  description = 'Python Rubix Cube GUI package',
	  author = 'David Grethlein',
	  author_email = '12dgrethlein@gmail.com',
	  url = 'https://github.com/dgrethlein/RubixCube' , 
	  download_url = 'https://github.com/dgrethlein/RubixCube/archive/v0.1.0.tar.gz',
	  keywords = ['Python', 'GUI', 'Rubix' , 'A*'],
	  install_requires = ['numpy' , 'pandas' , 'matplotlib'],
	  classifiers = ['Development Status :: 3 - Alpha',
	  	'Intended Audience :: Developers', 
	  	'Intended Audience :: End Users/Desktop', 
	  	'Topic :: Games/Entertainment :: Arcade',
	  	'License :: OSI Approved :: MIT License',
	  	'Programming Language :: Python :: 3.7',
	  ],
)