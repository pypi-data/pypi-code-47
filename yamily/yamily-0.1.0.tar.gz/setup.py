# yamify - define family trees in YAML
#
# Copyright (C) 2020 Fabian Peter Hammerle <fabian@hammerle.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pathlib

import setuptools

setuptools.setup(
    name="yamily",
    use_scm_version=True,
    packages=setuptools.find_packages(),
    description="Define family trees in YAML",
    long_description=pathlib.Path(__file__).parent.joinpath("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Fabian Peter Hammerle",
    author_email="fabian@hammerle.me",
    url="https://git.hammerle.me/fphammerle/yamily",
    license="GPLv3+",
    keywords=["ancestors", "family-tree", "genealogy", "plot", "visualize",],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Database",
        "Topic :: Sociology :: Genealogy",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": [
            "yamily-dot = yamily._cli:_dot",
            "yamily-list = yamily._cli:_list",
        ]
    },
    install_requires=[],
    extras_require={
        # >= 0.7 subgraph context manager
        "graphviz": ["graphviz>=0.7"],
        "yaml": ["PyYAML"],
    },
    setup_requires=["setuptools_scm"],
    tests_require=["pytest"],
)
