import os
import setuptools
from word_search_puzzle import __version__


def load_resource(path: str) -> str:
    with open(os.path.join('.', path), 'r') as file_resource:
        return file_resource.read()


# Package classifiers
PACKAGE_PROGRAMMING_LANGUAGE = 'Programming Language :: Python :: 3'
PACKAGE_LICENSE = 'License :: OSI Approved :: MIT License'
PACKAGE_OS = 'Operating System :: OS Independent'
PACKAGE_DEVELOPMENT_STATUS_PLANNING = 'Development Status :: 1 - Planning'
PACKAGE_DEVELOPMENT_STATUS_PRE_ALPHA = 'Development Status :: 2 - Pre-Alpha'
PACKAGE_DEVELOPMENT_STATUS_ALPHA = 'Development Status :: 3 - Alpha'
PACKAGE_DEVELOPMENT_STATUS_BETA = 'Development Status :: 4 - Beta'
PACKAGE_DEVELOPMENT_STATUS_PROD = 'Development Status :: 5 - Production/Stable'
PACKAGE_TOPIC_PUZZLE_GAMES = 'Topic :: Games/Entertainment :: Puzzle Games'

# Packages setup details
PACKAGE_NAME = 'word-search-puzzle'
PACKAGE_VERSION = __version__
PACKAGE_AUTHOR = 'Mohamad Karam Kassem'
PACKAGE_AUTHOR_EMAIL = 'karam.kass@gmail.com'
PACKAGE_DESCRIPTION = 'Word Search Puzzle Generator'
PACKAGE_DESCRIPTION_LONG = load_resource('README.md')
PACKAGE_DESCRIPTION_LONG_CONTENT_TYPE = 'text/markdown'
PACKAGE_REPOSITORY_URL = 'https://gitlab.com/kilobaik/word-search-puzzle/tree/master'


setuptools.setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    author=PACKAGE_AUTHOR,
    author_email=PACKAGE_AUTHOR_EMAIL,
    description=PACKAGE_DESCRIPTION,
    long_description=PACKAGE_DESCRIPTION_LONG,
    long_description_content_type=PACKAGE_DESCRIPTION_LONG_CONTENT_TYPE,
    url=PACKAGE_REPOSITORY_URL,
    packages=setuptools.find_packages(),
    classifiers=[
        PACKAGE_PROGRAMMING_LANGUAGE,
        PACKAGE_LICENSE,
        PACKAGE_OS,
        PACKAGE_TOPIC_PUZZLE_GAMES,
        PACKAGE_DEVELOPMENT_STATUS_PROD
    ],
    python_requires='>=3.6',
)