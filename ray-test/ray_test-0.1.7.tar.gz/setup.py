"""Describe our module distribution to Distutils."""

# Import third-party modules
import os
import sys
from shutil import rmtree
from setuptools import find_packages, Command
from setuptools import setup

NAME = 'ray_test'
DESCRIPTION = 'A Python-based API for Using Renderbus cloud rendering service.'
URL = 'https://github.com/renderbus/rayvision_api'
EMAIL = 'developer@rayvision.com'
AUTHOR = 'RayVision'
REQUIRES_PYTHON = '>=2.7.10,>=3.6.0'


def parse_requirements(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()


here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        # self.status('Pushing git tags…')
        # os.system('git tag v{0}'.format(about['__version__']))
        # os.system('git push --tags')

        sys.exit()


setup(
    name=NAME,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    version='0.1.7',
    package_dir={'': '.'},
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={},
    python_requires=REQUIRES_PYTHON,
    install_requires=list(parse_requirements('requirements.txt')),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    # use_scm_version=True,
    setup_requires=['setuptools_scm'],
    cmdclass={
        'upload': UploadCommand,
    }
)
