from setuptools import setup, find_packages
  
# reading long description from file 
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

  
# specify requirements of your package here 
REQUIREMENTS = [
'math'

] 
  
# some more details 
CLASSIFIERS = [ 
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers', 
    'Topic :: Scientific/Engineering :: Mathematics', 
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3.0', 
    ] 
  
# calling the setup function  
setup(name='complex', 
      version='0.1.0', 
      description='Compute complex numbers operations such as addition, substraction, multiplication , division and modulus.', 
      long_description=long_description, 
      long_description_content_type='text/markdown',
      url='https://github.com/deepak7376/complex', 
      author='Deepak Yadav', 
      author_email='dky.united@gmail.com', 
      license='MIT', 
      packages=find_packages(), 
      classifiers=CLASSIFIERS, 
      install_requires=REQUIREMENTS, 
      keywords='Complex Operations',
      include_package_data=True,
      zip_safe=False,
      python_requires='>=3'

      ) 