# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:11:37 2020

@author: Harmeet Kaur
"""

from distutils.core import setup
setup(
  name = '101703214_assign1_UCS633',         # How you named your package folder (MyLib)
  packages = ['101703214_assign1_UCS633'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='mit',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'TYPE YOUR DESCRIPTION HERE',   # Give a short description about your library
  author = 'Harmeet kaur',                   # Type in your name
  author_email = 'kaur.harmeet511@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/harmeet511/101703214_assign1_UCS633',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/harmeet511/101703214_assign1_UCS633/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['topsis', 'ucs633'],   # Keywords that define your package best
  install_requires=['numpy'  ],          # I get to this in a second
    
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
