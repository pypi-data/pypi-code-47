"""Setup for the caribouce package."""

import setuptools


README = "This is a test library created by Cederic Bosmans "

setuptools.setup(
    author="Cederic Bosmans",
    author_email="mail@gmail.com",
    name='ceribou',
    license="MIT",
    description='ceribou is a python package for delicious ceribou recipes.',
    version='v0.0.4',
    long_description=README,
    url='https://github.com/Bosmansc/Caribouce',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['requests'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)