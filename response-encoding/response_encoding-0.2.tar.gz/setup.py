
from distutils.core import setup

setup(
  name = 'response_encoding',         # How you named your package folder (MyLib)
  packages = ['response_encoding'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='GNU GENERAL PUBLIC LICENSE',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'It calculates response ratio of each category for every Target Label. One column per target class is returned.',   # Give a short description about your library
  author = 'Vivek Purkayastha',                   # Type in your name
  author_email = 'vivpur88@gmail.com',      # Type in your E-Mail
  url = 'https://https://github.com/gunnerVivek/response_encoding',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/gunnerVivek/response_encoding/archive/v0.2.tar.gz',
  keywords = ['Data Preprocessing', 'Response Coding', 'Data Science'],   # Keywords that define your package best
  install_requires=['numpy', 'pandas'], # dependencies,
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3.6'      #Specify which pyhton versions that you want to support
  ]
)
#'License :: OSI Approved :: GPL-3.0',   # Again, pick a license