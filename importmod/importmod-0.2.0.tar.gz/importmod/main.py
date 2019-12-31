# Copyright 2019 Portmod Authors
# Distributed under the terms of the GNU General Public License v3

import os
import sys
import urllib
import argparse
import traceback
import json
from portmod.log import err
from .generate import generate_build_files


def main():
    parser = argparse.ArgumentParser(
        description="Interface for creating partial pybuilds from a small amount of \
        information"
    )
    parser.add_argument(
        "import_mods",
        metavar="FILE",
        help='automatically generates pybuilds for mods specified in the given file. \
        File can be one of the following formats: \nA plaintext file consisting of a \
        mod atom and url per line, separated by a space. \nA json file with any of the \
        fields "atom", "name", "desc"/"description", "homepage", "category", "url", \
        "file"',
    )
    parser.add_argument(
        "-n",
        "--noreplace",
        help="Skips importing mods that have already been installed",
        action="store_true",
    )
    parser.add_argument(
        "-a",
        "--allow-failures",
        help="allows importing a mod even if a nonessential part of the import \
        procedure fails, such as failing to find a dependency for a plugin.",
        action="store_true",
    )
    parser.add_argument(
        "-V",
        "--validate",
        help="Checks hashes of downloaded files if they were provided",
        action="store_true",
    )

    parser.add_argument("--debug", help="Enables debug traces", action="store_true")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()

    (mod_name, ext) = os.path.splitext(os.path.basename(args.import_mods))
    parsedurl = urllib.parse.urlparse(args.import_mods)
    print(parsedurl)
    failed = []

    with open(args.import_mods, mode="r") as file:
        if ext == ".json":
            mods = json.load(file)
            for index, mod in enumerate(mods):
                print(f"Importing mod {index}/{len(mods)}")
                try:
                    generate_build_files(
                        mod, args.noreplace, args.allow_failures, args.validate
                    )
                except Exception as e:
                    if args.debug:
                        traceback.print_exc()
                    err("{}".format(e))
                    failed.append(mod)
        else:
            for line in file.readlines():
                words = line.split()
                if len(words) > 0:
                    d = {"atom": words[0], "url": words[1]}
                    try:
                        generate_build_files(
                            d, args.noreplace, args.allow_failures, args.validate,
                        )
                    except Exception as e:
                        if args.debug:
                            traceback.print_exc()
                        err("{}".format(e))
                        failed.append(d)
    if failed:
        err("The following mods failed to import:")
        print("\n".join(["{}".format(f.get("name", f["atom"])) for f in failed]))
