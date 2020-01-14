# coding: utf-8
'''
This file is part of the `cn_workday` Python package.
'''
import os
import os.path
import setuptools

with open('README.md', 'r') as rf:
    long_description = rf.read()

data_files = []
for dirpath, dirnames, filenames in os.walk(os.path.join('cn_workday', 'data')):
    base = dirpath.split(os.path.sep, 1)[-1]
    data_files.extend([os.path.join(base, fname) for fname in filenames])

setuptools.setup(
    name='cn_workday',
    version='2020.01.14.2',
    author='Joker Qyou',
    description='Workday detection for China',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JokerQyou/cn_workday',
    packages=setuptools.find_packages(),
    package_data={
        'cn_workday': data_files,
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'pytz>=2019.3',
    ],
)

