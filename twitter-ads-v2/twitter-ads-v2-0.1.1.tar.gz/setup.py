import os
from setuptools import setup, find_packages

DESCRIPTION = 'Twitter Ads API SDK for Python.'
URL = 'https://github.com/smaeda-ks/twitter-python-ads-sdk-v2'
DOWNLOAD_URL = 'https://github.com/smaeda-ks/twitter-python-ads-sdk-v2/tarball/master'


def readme():
    with open('README.md') as f:
        return f.read()


def get_version(version_tuple):
    if not isinstance(version_tuple[-1], int):
        return '.'.join(map(str, version_tuple[:-1])) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))


init = os.path.join(os.path.dirname(__file__), 'twitter_ads_v2', '__init__.py')
version_line = list(filter(lambda l: l.startswith('VERSION'), open(init)))[0]
VERSION = get_version(eval(version_line.split('=')[-1]))

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Internet',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

extra_opts = {
    'setup_requires': ['flake8==3.7.7', 'pytest-runner'],
    'tests_require': ['pytest', 'responses', 'mock'],
    'extras_require': {
        'doc': ['sphinx>=2.0.0, <3.0.0', 'sphinx-rtd-theme', 'm2r']
    }
}

setup(
    name='twitter-ads-v2',
    version=VERSION,
    author='Shohei Maeda',
    url=URL,
    download_url=DOWNLOAD_URL,
    license='MIT',
    include_package_data=True,
    description=DESCRIPTION,
    long_description=readme(),
    long_description_content_type='text/markdown',
    platforms=['any'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'python-dateutil',
        'oauthlib==3.1.0',
        'requests'
    ],
    packages=find_packages(exclude=['docs', 'tests']),
    **extra_opts
)
