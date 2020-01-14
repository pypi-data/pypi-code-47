#! /usr/bin/env python

import os
from argparse import ArgumentParser


def run():
    parser = ArgumentParser("Deploy Utilities")
    parser.add_argument("-d", action="store_true")
    parser.add_argument("-v", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("tag", nargs='?')

    args = parser.parse_args()

    files_to_include = []

    # Find available files
    base_file = 'docker-compose.yml'
    if not os.path.exists(base_file):
        print(f"Could not find '{base_file}'")
        exit(1)

    files_to_include.append(base_file)

    # Parse environment
    if not args.tag:
        environment = 'deploy'
        tags = ['deploy'] if os.path.exists('docker-compose.deploy.yml') else []
    else:
        # Strip prefix and suffix if it is a file
        tags = args.tag.split(".")
        if os.path.exists(args.tag):
            tags = tags[1:-1]

        environment = tags[0]
        tags = ['.'.join(tags[:(x+1)]) for x in range(len(tags))]

    for t in tags:
        additional = f'docker-compose.{t}.yml'
        if not os.path.exists(additional):
            print(f"Could not find '{additional}'")
            exit(1)
        files_to_include.append(additional)

    flags = ["--force-recreate", "--renew-anon-volumes", "--build"]

    if environment == 'deploy' or args.d:
        flags.append("-d")

    # We build command
    cmd = f'docker-compose -p {environment} -f {" -f ".join(files_to_include)} up {" ".join(flags)}'

    if args.v:
        print(cmd)

    if not args.dry_run:
        os.system(cmd)


if __name__ == "__main__":
    run()
