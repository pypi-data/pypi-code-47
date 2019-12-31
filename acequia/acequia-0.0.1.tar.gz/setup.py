

import setuptools

setuptools.setup(
    name="acequia",
    version="0.0.1",
    description='Tools for managing data flow of groundwater series',
    url='https://github.com/tdmeij/acequia.git',
    author='Thomas de Meij',
    author_email='woestenboe@gmail.com',
    license='MIT',
    keywords = ['statistics', 'math'],
    classifiers = [
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Hydrology',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'Topic :: Utilities'
        ],
    packages=setuptools.find_packages(),
)
