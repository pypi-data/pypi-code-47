import os
from setuptools import setup
from Cython.Build import cythonize
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), "r") as f:
    long_description = f.read()

setup(
    name='BioMetaDB',
    version='0.1.2.7',
    description='Use biological data to generate SQL database schema',
    url="https://github.com/cjneely10/BioMetaDB",
    author="Christopher Neely",
    author_email="christopher.neely1200@gmail.com",
    license="GNU GPL 3",
    requires=['biopython', 'Cython', 'SQLAlchemy'],
    python_requires='>=3.6',
    ext_modules=cythonize(["*/*/*.pyx", ]),
)

