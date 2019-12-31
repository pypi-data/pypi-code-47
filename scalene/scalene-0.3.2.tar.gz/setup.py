from setuptools import setup, find_packages

setup(name='scalene',
      version='0.3.2',
      description='Scalene: A high-resolution, low-overhead CPU and memory profiler for Python',
      long_description='README.md',
      long_description_content_type="text/markdown",
      url='https://github.com/emeryberger/scalene',
      author='Emery Berger',
      author_email='emery@cs.umass.edu',
      license='Apache License 2.0',
          classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent",
     ],
      packages=find_packages()
)
