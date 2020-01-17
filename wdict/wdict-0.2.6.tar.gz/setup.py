from setuptools import setup, find_packages
from wdict import __version__

REQUIRES = ["numpy"]
CLASSIFIERS = [
    "License :: OSI Approved :: MIT License",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Operating System :: OS Independent",
    "Topic :: Software Development"]

setup(
    name='wdict',
    version=__version__,
    description='extended dictionary class',
    url='https://github.com/shinaji/wdict',
    author='shinaji',
    author_email='shina.synergy@gmail.com',
    license='MIT',
    keywords='dict',
    packages=find_packages(),
    install_requires=REQUIRES,
    classifiers=CLASSIFIERS,
)
