# -*- coding: utf-8 -*-

"""Console script for reqchecker."""
import argparse
import sys
import os
from reqchecker.reqchecker import logsetup, checklist, empty_requirements
from reqchecker.checkers import check_sources, print_conflicts

def main():
    """Console script for reqchecker."""

    parser = argparse.ArgumentParser()

    parser.add_argument('--file', '--file', dest='file', type=str,
                        help="Path to json file to use, other than "
                        "reqchecker/defaults.json.")

    parser.add_argument('--section', '--section', dest='section', type=str,
                        default='default', help="defaults.json section to use.")

    # These will replace defaults.json if supplied
    parser.add_argument('--source', '--source', dest='source', type=str,
                        choices = ["github", "local"],
                        help="Source to check. If 'local', must also supply "
                        "--locations and --packages.")

    parser.add_argument('--locations', '--locations', dest='locations', type=str,
                        nargs='+', help="Paths to packages. If using --source "
                        "local, must also use --locations and --packages")

    parser.add_argument('--packages', '--packages', dest='packages', type=str,
                        nargs='+', help="Package names. If using --source "
                        "local, must also use --locations and --packages")

    parser.add_argument('--branches', '--branches', dest='branches', type=str,
                        nargs='+', help="Branches to packages to use with "
                        "--source 'github' option.")

    parser.add_argument('--debug','-nd', dest='debug', action='store_true',
                        help="Debug log level")

    args = parser.parse_args()

    # Set up logging
    logger = logsetup(args.debug)
    logger.info(" reqchecker gonna check yo reqs")

    lp = [args.locations, args.packages, args.branches]

    if not os.path.isfile(args.file):
        logger.error("Given --file {} not a valid file".format(args.file))

    if args.source == "local" and None in [args.locations, args.packages]:
        logger.error(" Must include --locations and --packages when supplying "
            "--source 'local' ")
        exit()

    if args.source == "github" and None in [args.branches, args.packages]:
        logger.error(" Must include --bramches and --packages when supplying "
            "--source 'github' ")
        exit()

    if sum(x is not None for x in lp) == 1:
        logger.error(" Must supply both --packages and --locations when using "
            "local, or --packages and --branches when using github")
        exit()

    # Set up options dashboard to check from
    options = {"file": args.file,
        "section": args.section,
        "source": args.source,
        "locations": args.locations,
        "packages": args.packages,
        "branches": args.branches,}

    # Get options from cli args and defaults
    check_list = checklist(options, logger)

    # Make an empty requirements list from the sources
    requirements = empty_requirements(check_list)

    # Check all of the sources
    requirements = check_sources(check_list, requirements, logger)

    # Print duplicates and conflicts
    print_conflicts(requirements, check_list)

    # Add sage advice
    logger.debug(" Make wise decisions!")

if __name__ == "__main__":
    sys.exit(main())
