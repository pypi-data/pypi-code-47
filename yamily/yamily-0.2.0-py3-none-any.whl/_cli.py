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

import argparse
import pathlib
import sys
import typing

import yaml

import yamily
import yamily._graphviz
import yamily.yaml


def _read(path: pathlib.Path) -> typing.Iterator[yamily.Person]:
    if path.is_dir():
        for file_path in path.glob("**/*.yml"):
            for person in _read(file_path):
                yield person
    else:
        with path.open("r") as yaml_file:
            yield yaml.load(yaml_file, Loader=yamily.yaml.Loader)


def _list() -> None:
    argparser = argparse.ArgumentParser(
        description="Recursively find yamily family tree members and print as YAML list."
    )
    argparser.add_argument(
        "paths", nargs="+", metavar="path", help="path to yamily .yml file or folder"
    )
    args = argparser.parse_args()
    collection = yamily.PersonCollection()
    for path in args.paths:
        for person in _read(pathlib.Path(path)):
            collection.add_person(person)
    yaml.dump(
        sorted(collection, key=lambda p: p.identifier),
        sys.stdout,
        Dumper=yamily.yaml.Dumper,
        default_flow_style=False,
        allow_unicode=True,
    )


def _dot() -> None:
    argparser = argparse.ArgumentParser(
        description="Create family tree in DOT (graphviz) format. "
        "Recursively looks for *.yml files containing family members in yamily format."
    )
    argparser.add_argument(
        "paths", nargs="+", metavar="path", help="path to yamily .yml file or folder"
    )
    argparser.add_argument("--comment", dest="comment_text")
    args = argparser.parse_args()
    collection = yamily.PersonCollection()
    for path in args.paths:
        for person in _read(pathlib.Path(path)):
            collection.add_person(person)
    graph = yamily._graphviz.digraph(collection)  # pylint: disable=protected-access
    if args.comment_text is not None:
        with graph.subgraph(name="cluster_comment") as comment:
            comment.attr(style="invisible")
            comment.node("comment", label=args.comment_text, shape="none")
    print(graph.source)
