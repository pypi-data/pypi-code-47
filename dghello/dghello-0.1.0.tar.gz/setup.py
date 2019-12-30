import setuptools

with open('README.md', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name = 'dghello', # name of package folder
  version = '0.1.0', # increase it with every release
  author = 'Daniel Groner',
  author_email = 'dgroner@fordham.edu',
  license='MIT', # Chose a license from here: https://help.github.com/articles/li
  description = 'Test package for github and PyPi', # a short description
  long_description=long_description,
  long_description_content_type='text/markdown',
  url = 'https://github.com/dgroner/dghello', # link to github
  packages=setuptools.find_packages(),
  keywords = ['DGHELLO', 'GRONER'], # Keywords for package
  install_requires=[
  ],
classifiers=[
  'Development Status :: 3 - Alpha', # "3 - Alpha", "4 - Beta" or "5
  'Intended Audience :: Developers', # Define that audience as developers
  'Topic :: Software Development :: Build Tools',   # TODO
  'License :: OSI Approved :: MIT License', # Again, pick a license
  'Programming Language :: Python :: 3', #Specify which python versions that you
  'Operating System :: OS Independent',
  ],
python_requires='>=3.6',
)
