"""Command line interface for YamlTable."""


import argparse
import pdb
import pprint
from typing import List, Optional

import fastjsonschema
import yamltable
from yamltable.typing import Row, Schema


def list_(args: argparse.Namespace, rows: List[Row], schema: Optional[Schema] = None) -> None:
    """List dictionary key values.

    :param args: command line arguments
    :param rows: YAML file dictionaries
    :param schema: JSON schema for YAML file
    """

    for idx, row in enumerate(rows):
        try:
            print(row[args.key])
        except KeyError:
            print(f"error: row {idx} does not have key {args.key}")
            break


def main() -> None:
    """Command line interface for YamlTable."""

    parser = argparse.ArgumentParser(
        description="utilities for working with list organized YAML files"
    )
    parser.add_argument("-d", "--debug", action="store_true", help="run yamltable in debug mode")
    parser.add_argument("-v", "--version", action="version")
    subparser = parser.add_subparsers(dest="command", required=True)

    list_parser = subparser.add_parser(
        name="list", description="list dictionary key values", help="list dictionary key values"
    )
    list_parser.add_argument("key", type=str, help="dictionary key")
    list_parser.add_argument("file_path", type=str, help="YAML file location")
    list_parser.set_defaults(func=list_)

    search_parser = subparser.add_parser(
        name="search",
        description="search dictionaries by key and value",
        help="search dictionaries by key and value",
    )
    search_parser.add_argument("key", type=str, help="dictionary key")
    search_parser.add_argument("value", help="key value")
    search_parser.add_argument("file_path", type=str, help="YAML file location")
    search_parser.set_defaults(func=search)

    sort_parser = subparser.add_parser(
        name="sort",
        description="sort dictionaries by key and value",
        help="sort dictionaries by key and value",
    )
    sort_parser.add_argument("key", type=str, help="dictionary key")
    sort_parser.add_argument("file_path", type=str, help="YAML file location")
    sort_parser.set_defaults(func=sort)

    validate_parser = subparser.add_parser(
        name="validate", description="validate dictionaries", help="validate dictionaries"
    )
    validate_parser.add_argument("file_path", type=str, help="YAML file location")
    validate_parser.set_defaults(func=validate)

    args = parser.parse_args()
    if args.debug:
        pdb.runcall(worker, args)
    else:
        worker(args)


def search(args: argparse.Namespace, rows: List[Row], schema: Optional[Schema] = None) -> None:
    """Search dictionaries for matching key and value.

    :param args: command line arguments
    :param rows: YAML file dictionaries
    :param schema: JSON schema for YAML file
    """

    for match in yamltable.search(args.key, args.value, rows):
        pprint.pprint(match, indent=2)


def sort(args: argparse.Namespace, rows: List[Row], schema: Optional[Schema] = None) -> None:
    """Sort dictionaries by key values.

    :param args: command line arguments
    :param rows: YAML file dictionaries
    :param schema: JSON schema for YAML file
    """

    try:
        sorted_rows = yamltable.sort(args.key, rows)
    except TypeError as xcpt:
        print(f"error: {xcpt}")
    else:
        yamltable.write(args.file_path, sorted_rows, schema)


def validate(args: argparse.Namespace, rows: List[Row], schema: Optional[Schema] = None) -> None:
    """Check that every dictionary has valid format.

    :param args: command line arguments
    :param rows: YAML file dictionaries
    :param schema: JSON schema for YAML file
    """

    if schema is not None:
        try:
            yamltable.validate(rows, schema)
        except fastjsonschema.JsonSchemaDefinitionException as xcpt:
            print(f"error: schema definition: {xcpt}")
    else:
        print("error: YAML file contains no schema")


def worker(args: argparse.Namespace) -> None:
    """Execute yamltable functionality

    :param args: command line arguments
    """

    try:
        rows, schema = yamltable.read(args.file_path)
    except TypeError as xcpt:
        print(xcpt)
    else:
        args.func(args, rows, schema)


if __name__ == "__main__":
    main()
