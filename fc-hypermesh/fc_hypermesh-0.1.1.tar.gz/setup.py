from setuptools import setup, find_packages
from os import path
import sys
here = path.abspath(path.dirname(__file__))


if sys.version_info[0]>2:
  with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
else:    
  with open(path.join(here, 'README.rst')) as f:  
    long_description = f.read().decode("UTF-8")


setup_defaults = {  
   'name'        : 'fc_hypermesh',
   'description' : 'Generate conforming meshes of hypercubes, hyperrectangles or of any d-orthotopes by simplices or orthotopes with their m-faces',
   'version'     : '0.1.1',
   'url'         : 'http://www.math.univ-paris13.fr/~cuvelier/software',
   'author'      : 'Francois Cuvelier',
   'author_email': 'cuvelier@math.univ-paris13.fr',
   'license'     : 'BSD',
   'packages'    : ['fc_hypermesh'],
   'classifiers':['Topic :: Scientific/Engineering :: Mathematics'],
   } 

# needs numpy >= 1.14.0
fc_install_requires=['fc_tools >= 0.0.24', 'fc_bench >= 0.2.0'] # automaticaly written by setpackages.py script

setup(name=setup_defaults['name'],
      description = setup_defaults['description'],
      long_description=long_description,
      long_description_content_type='text/x-rst',
      version=setup_defaults['version'],
      url=setup_defaults['url'],
      author=setup_defaults['author'],
      author_email=setup_defaults['author_email'],
      license = setup_defaults['license'],
      packages=setup_defaults['packages'],
      classifiers=setup_defaults['classifiers'],
      install_requires=['numpy']+fc_install_requires
     )
