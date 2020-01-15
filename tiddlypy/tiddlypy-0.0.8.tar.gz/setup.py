from distutils.core import setup
setup(
  name = 'tiddlypy',
  packages = ['tiddlypy'],
  version = '0.0.8',
  license='wtfpl',
  description = 'Simple server for local TiddlyWiki',
  author = 'octopus.io',
  author_email = 'pypi@octopus.io',
  url = 'https://gitlab.com/octopus.io/tiddlypy',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['TiddlyWiki'],
  scripts = [],
  entry_points={"console_scripts": ["tiddlypy=tiddlypy.main:main_func"]},
  install_requires=[
          'wheel',
          'Flask'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
  ],
)
