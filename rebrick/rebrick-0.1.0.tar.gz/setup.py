#  Created by Martin Strohalm

from setuptools import setup, find_packages

# get version
from rebrick import version
version = '.'.join(str(x) for x in version)

# include additional files
package_data = {}

# set classifiers
classifiers = [
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 3 :: Only',
    'Operating System :: OS Independent',
    'Topic :: Utilities',
    'Intended Audience :: Other Audience']

# main setup
setup(
    name = 'rebrick',
    version = version,
    description = 'Python access to Rebrickable API.',
    url = 'https://github.com/xxao/rebrick',
    author = 'Martin Strohalm',
    author_email = 'rebrick@bymartin.cz',
    license = 'MIT',
    packages = find_packages(),
    package_data = package_data,
    classifiers = classifiers,
    install_requires = [],
    zip_safe = False)
