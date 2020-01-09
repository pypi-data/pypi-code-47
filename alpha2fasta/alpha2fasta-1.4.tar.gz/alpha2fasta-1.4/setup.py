from setuptools import setup, find_packages
 
setup(name='alpha2fasta',
      version='1.4',
#      url='https://github.com/diogomachado-bioinfo/alpha2fasta',
      author='Diogo de Jesus Soares Machado',
      author_email='diogomachado.bioinfo@gmail.com',
      description='Encode text written in natural language in a FASTA-based format',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.rst').read(),
      zip_safe=False)