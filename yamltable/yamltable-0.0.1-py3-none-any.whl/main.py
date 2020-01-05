"""Command line interface for YamlTable."""


import argparse
import pprint

import yamltable


def main() -> None:
    """Command line interface for YAML sorter."""

    parser = argparse.ArgumentParser(
        description="utilities for for working with list organized YAML files"
    )
    subparser = parser.add_subparsers(dest="command", required=True)

    list_parser = subparser.add_parser(name="list", description="list dictionary key values")
    list_parser.add_argument("key", type=str, help="dictionary key")
    list_parser.add_argument("file_path", type=str, help="YAML file location")

    search_parser = subparser.add_parser(
        name="search", description="search dictionaries by key and value"
    )
    search_parser.add_argument("key", type=str, help="dictionary key")
    search_parser.add_argument("value", help="key value")
    search_parser.add_argument("file_path", type=str, help="YAML file location")

    sort_parser = subparser.add_parser(
        name="sort", description="sort dictionaries by key and value"
    )
    sort_parser.add_argument("key", type=str, help="dictionary key")
    sort_parser.add_argument("file_path", type=str, help="YAML file location")

    args = parser.parse_args()
    dicts = yamltable.read(args.file_path)

    if args.command == "list":
        for dict_ in dicts:
            print(dict_[args.key])
    elif args.command == "search":
        for match in yamltable.search(args.key, args.value, dicts):
            pprint.pprint(match)
    elif args.command == "sort":
        sorted_dicts = yamltable.sort(args.key, dicts)
        yamltable.write(args.file_path, sorted_dicts)


if __name__ == "__main__":
    main()
