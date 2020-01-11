#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages
import sys
import os
import re

if sys.version_info < (3, 7, 0):
  print("Python 3.7+ is required")
  exit(1)

with open("requirements.txt") as file:
  requirements = file.read().splitlines()[1:]
git_requirements = list(filter(lambda x: x.startswith("git+"), requirements))
requirements = list(set(requirements).difference(git_requirements))

CURDIR = os.path.abspath(os.path.dirname(__file__))

def get_version():
  main_file_path = os.path.join(CURDIR, "src", "prman", "main.py")
  with open(main_file_path, "r") as f:
    main_file = f.read()
  match = re.search(r"__version__ = \"(?P<version>.+?)\"", main_file)
  assert not match is None
  return match.group("version")

def get_readme():
  readme_path = os.path.join(CURDIR, "README.md")
  with open(readme_path, "r") as f:
    return f.read()


setup(
  name="prman",
  version=get_version(),
  description="Command line tool for automatic GitLab PR creation.",
  long_description=get_readme(),
  long_description_content_type="text/markdown",
  license="Unlicense",
  author="Ilya Latushko",
  author_email="ilyalatt@gmail.com",
  url="https://github.com/ilyalatt/prman",
  include_package_data=True,
  packages=find_packages(where="src"),
  package_dir={"": "src"},
  install_requires=requirements,
  dependency_links=git_requirements,
  python_requires=">=3.7",
  zip_safe=False,
  entry_points={"console_scripts": ["prman=prman.main:main"]},
)
