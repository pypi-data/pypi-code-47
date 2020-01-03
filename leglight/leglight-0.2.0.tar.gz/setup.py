import setuptools
import os
import sys
from codecs import open

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'leglight', '__version__.py'), 'r', 'utf-8') as f:
    x = f.read()
    exec(x, about)

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=about['__url__'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
    ],
    python_requires='>=3.6',
    keywords=["elgato", "key light", "corsair"],
    install_requires=["zeroconf>=0.24.3", "requests>=2.22.0"],
    platforms=['unix', 'linux', 'osx']
)