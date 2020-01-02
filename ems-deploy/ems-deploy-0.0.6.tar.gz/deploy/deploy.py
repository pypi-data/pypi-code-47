#! /usr/bin/env python

import os
from argparse import ArgumentParser


def run():
    parser = ArgumentParser("Deploy Utilities")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("-d", action="store_true")
    parser.add_argument("-v", action="store_true")

    args = parser.parse_args()

    # Find available files
    base_file = 'docker-compose.yml'
    if not os.path.exists(base_file):
        print(f"Could not find '{base_file}'")
        exit(1)

    environment = "debug" if args.debug else "deploy"

    additonal = f"docker-compose.{environment}.yml"
    if not os.path.exists(additonal):
        print(f"Could not find '{additonal}'")
        exit(1)

    flags = ["--force-recreate", "--renew-anon-volumes", "--build"]

    if not args.debug or args.d:
        flags.append("-d")

    # We build command
    cmd = f'docker-compose -p {environment} -f {base_file} -f {additonal} up {" ".join(flags)}'

    if args.v:
        print(cmd)

    os.system(cmd)
