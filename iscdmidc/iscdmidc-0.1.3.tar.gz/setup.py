"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

import iscdmidc

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
setup(
    name="iscdmidc",
    version=iscdmidc.__version__,
    description="python lib that parse the output of dmidecode ",
    long_description=long_description,
    license='MIT',
    url = "https://github.com/HanPeng1104/iscdmidc",
    author = "hanpeng",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
    py_modules=["iscdmidc"],
    install_requires=[],
    package_data={},
    data_files=[],
    entry_points={},
    )