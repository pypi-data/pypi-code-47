import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'topsis_by_van',         # How you named your package folder (MyLib)
  packages = ['topsis_by_van'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Topsis',   # Give a short description about your library
  author = 'Vanshika Angi',                   # Type in your name
  author_email = 'angivanshikaangi@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/vanshika-angi/topsis',   # Provide either the link to your github or to your website    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],
  include_package_data=True,

  install_requires=[            # I get to this in a second
          'numpy'
      ],
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
