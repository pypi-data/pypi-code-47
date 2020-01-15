import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'salamander',         # How you named your package folder (MyLib)
  packages=['salamander'],
  version = 'v1.2',      # Start with a small number and increase it with every change you make
  license='gpl-3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Genetic algorithm library for humans',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Rayen Mhamdi',                   # Type in your name
  author_email = 'rayenmhamdi94@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/rayenmhamdi/salamander',   # Provide either the link to your github or to your website
  keywords = ['salamander', 'Genetic Algorithm', 'Chromosome', 'Individuals', 'Population'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',   # Again, pick a license
  ],
  python_requires='>=3.',
)