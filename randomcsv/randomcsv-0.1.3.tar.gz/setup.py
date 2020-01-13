from glob import glob
from os.path import splitext, basename

from setuptools import find_packages
from setuptools import setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='randomcsv',
    version='0.1.3',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    url='https://github.com/PhilipBuhr/randomCsv',
    download_url='https://github.com/PhilipBuhr/randomCsv/archive/0.1.0.tar.gz',
    license='MIT',
    author='Philip Buhr',
    author_email='philip.buhr@buhrwerk.de',
    description='For generating specific CSVs for testing data piplines',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['pandas', 'requests', 'pytest', 'numpy'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
