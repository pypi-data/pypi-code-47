"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

__version__ = '0.0.8'

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=tflow', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name = 'tflow',
    version = __version__,
    description = 'A CLI for deploying a model with the Trell Model Pipeline.',
    long_description = long_description,
    url = 'https://github.com/frisellcpl/tflow',
    author = 'Johan Frisell',
    author_email = 'johan@trell.se',
    license = 'MIT',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    package_data = {'tflow': ['gitlab-ci.tmpl']},
    install_requires = ['mako'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'tflow=tflow.cli:main',
        ],
    },
    cmdclass = {'test': RunTests},
)
