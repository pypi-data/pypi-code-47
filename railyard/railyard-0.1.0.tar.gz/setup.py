# -*- coding: utf-8 -*-

# Copyright (c) 2020, Brandon Nielsen
#
# This file is part of Railyard.
#
# Railyard is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Railyard is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Railyard.  If not, see <https://www.gnu.org/licenses/>.

from os import path

from setuptools import find_packages, setup

from railyard import __version__

THIS_DIRECTORY = path.abspath(path.dirname(__file__))
with open(path.join(THIS_DIRECTORY, "README.rst"), encoding="utf-8") as f:
    README_TEXT = f.read()

setup(
    name="railyard",
    version=__version__,
    description="Simple local application development server",
    long_description=README_TEXT,
    long_description_content_type="text/x-rst",
    author="Brandon Nielsen",
    author_email="nielsenb@jetfuse.net",
    url="https://bitbucket.org/nielsenb/railyard",
    entry_points={"console_scripts": ["railyard = railyard.entrypoint:main",]},
    python_requires=">=3.7",
    install_requires=["gunicorn", "pyyaml"],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="webapp dispatch routing",
    project_urls={
        "Documentation": "https://railyard.readthedocs.io/en/latest/",
        "Source": "https://bitbucket.org/nielsenb/railyard",
        "Tracker": "https://bitbucket.org/nielsenb/railyard/issues",
    },
)
