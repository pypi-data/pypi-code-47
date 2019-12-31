#!/usr/bin/env python

# Copyright 2019 Portmod Authors
# Distributed under the terms of the GNU General Public License v3


from setuptools import setup, find_packages

setup(
    name="importmod",
    author="Portmod Authors",
    description="A CLI tool to import mods into the Portmod repository format",
    license="GPLv3",
    url="https://gitlab.com/portmod/importmod",
    packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
    entry_points=({"console_scripts": ["omwimport = importmod.main:main"]}),
    install_requires=["portmod", "gitpython", "requests", "patool"],
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
)
