
from distutils.core import setup
setup(
  name = 'copywise',         # How you named your package folder (MyLib)
  packages = ['copywise'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Wisely copy files',   # Give a short description about your library
  author = 'Matheus Couto',                   # Type in your name
  author_email = 'matheusccouto@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/matheusccouto/copywise',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/matheusccouto/copywise/archive/1.0.tar.gz',    # I explain this later on
  keywords = ['COPY', 'EXTENSION'],   # Keywords that define your package best
  classifiers=[
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.6',
  ],
)