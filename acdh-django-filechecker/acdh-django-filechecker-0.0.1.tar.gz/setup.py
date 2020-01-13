import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='acdh-django-filechecker',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Django-App to store, edit, enrich and serialize the results of repo-file-checker',
    long_description=README,
    url='https://github.com/acdh-oeaw/acdh-django-filechecker',
    author='Peter Andorfer',
    author_email='peter.andorfer@oeaw.ac.at',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'acdh-django-archeutils>=0.0.1',
        'acdh-django-netvis>=0.1.1',
        'Django>=3.0',
        'django-mptt>=0.10.0'
        'rdflib>=4.2.2',
    ],
)
