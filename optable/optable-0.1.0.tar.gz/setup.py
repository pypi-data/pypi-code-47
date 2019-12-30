import setuptools

with open('README.md', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name = 'optable', # name of package
  version = '0.1.0',
  author = 'Daniel Groner',
  author_email = 'dgroner@fordham.edu',
  license='MIT',
  description = 'Math programming using pandas', # short description
  long_description=long_description,
  long_description_content_type='text/markdown',
  url = 'https://github.com/dgroner/optable', # link to github
  packages=setuptools.find_packages(),
  keywords = ['LINEAR PROGRAMMING', 'MATH PROGRAMMING', 'OPTIMIZATION'], # Keywords for package
  install_requires=['scipy>=1.0.0'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.0',
)
