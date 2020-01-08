from os import path
from setuptools import setup


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pysqlite3tool',
    version='0.0.1a',
    packages=['pysqlite3tool'],
    url='https://github.com/c-pher/SQLite3Tool.git',
    license='MIT',
    author='Andrey Komissarov',
    author_email='a.komisssarov@gmail.com',
    description='The cross-platform tool to work with SQLite3 database',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Systems Administration',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3.6',
)
