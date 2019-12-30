from distutils.core import setup
from setuptools import find_packages
import codecs

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'StarkLego',         # How you named your package folder (MyLib)
    packages=find_packages(),
    version = '0.1.6',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Library used to create lego builds',   # Give a short description about your library
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Petar Kenic',                   # Type in your name
    author_email = 'kenicpetar@yahoo.com',      # Type in your E-Mail
    url = 'https://github.com/peken97/StarkLego',   # Provide either the link to your github or to your website
    keywords = ['LEGO', 'BUILD', 'LDRAW'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
            'gym',
            'pyldraw',
            'numpy==1.16.0',
            'tensorflow==1.8.0'
      ],
    classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.5',      #Specify which pyhton versions that you want to support
    
  ],
)