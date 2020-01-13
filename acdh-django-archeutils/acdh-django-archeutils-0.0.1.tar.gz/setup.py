import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='acdh-django-archeutils',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description='Utility module to serialize a django-model into ARCHE-RDF.',
    long_description=README,
    url='https://github.com/acdh-oeaw/acdh-django-archeutils',
    author='Peter Andorfer',
    author_email='peter.andorfer@oeaw.ac.at',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'Django>=3.0',
        'rdflib>=4.2.2',
    ],
)
