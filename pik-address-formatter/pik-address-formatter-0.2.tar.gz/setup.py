# To use a consistent encoding
from codecs import open as codec_open
from os import path
# Always prefer setuptools over distutils
from setuptools import setup, find_packages

HERE_PATH = path.abspath(path.dirname(__file__))

with open(path.join(HERE_PATH, 'README.md')) as readme_fd:
    LONG_DESCRIPTION = readme_fd.read()

with open(path.join(HERE_PATH, 'requirements.txt')) as req_fd:
    REQUIREMENTS = [
        line for line in req_fd.readlines()
        if line and not line.startswith('#')
    ]

setup(
    name='pik-address-formatter',
    version='0.2',
    author='pik-software',
    author_email='no-reply@pik-software.ru',
    description='Address formatter for address components from housing',
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/pik-software/pik-address-formatter.git',
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='apiqa',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=REQUIREMENTS,
    python_requires='~=3.6',
)
