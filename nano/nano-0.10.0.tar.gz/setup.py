#!/usr/bin/env python

from setuptools import setup, find_packages

README_FILE = open('README.rst')
try:
    long_description = README_FILE.read()
finally:
    README_FILE.close()

exclude = [
    'nanosite',
    'tests*',
    '*tests',
    '*.pyc',
    '*.pyo',
    '__pycache__',
]

packages=(
    'nano.activation',
    'nano.badge',
    'nano.blog',
    'nano.chunk',
    'nano.comments',
    'nano.countries',
    'nano.faq',
    'nano.mark',
    'nano.privmsg',
    'nano.tools',
    'nano.user',
)


setup(name='nano',
    version='0.10.0',
    packages=find_packages(exclude=exclude),
    include_package_data=True,
    zip_safe=False,
    platforms=['any'],
    description='Does less! Loosely coupled mini-apps for django.',
    author_email='kaleissin@gmail.com',
    author='kaleissin',
    long_description=long_description,
    url='https://github.com/kaleissin/django-nano',
    python_requires='>=2.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
