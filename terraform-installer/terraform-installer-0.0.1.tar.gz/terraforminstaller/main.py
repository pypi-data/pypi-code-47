#!/usr/bin/env python

"""install or update to the latest version of terraform"""

import argparse
from argparse import RawTextHelpFormatter as rawtxt
import sys
import signal
import json
import os
import platform as sysplat
import subprocess
import pkg_resources
from stringcolor import *

def signal_handler(sig, frame):
    """handle control c"""
    print('\nuser cancelled')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def query_yes_no(question, default="yes"):
    '''confirm or decline'''
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("\nPlease respond with 'yes' or 'no' (or 'y' or 'n').\n")

def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""
    from shutil import which
    return which(name) is not None

def main():
    '''install or update to the latest version of terraform'''
    version = pkg_resources.require("terraform-installer")[0].version
#    version = "0.0.0"
    parser = argparse.ArgumentParser(
        description='install or update to the latest version of terraform',
        prog='terraform-installer',
        formatter_class=rawtxt
    )

    #parser.print_help()
    parser.add_argument(
        "platform",
        help=""".\n\n
    $ terraform-installer linux_amd64\n
    options are [darwin_amd64, freebsd_386, freebsd_amd64, freebsd_arm, linux_386, linux_amd64, linux_arm, openbsd_386, openbsd_amd64, solaris_amd64, windows_386, windows_amd64]""",
        nargs='?',
        default='none'
    )
    parser.add_argument('--key', help="optional. use a tag key besides Name", default="Name")
    parser.add_argument('-g', '--green', action='store_true', help='start.')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s '+version)
    args = parser.parse_args()
    platform = args.platform
    green = args.green
    do_nothing = False
    # check for aws
    if not is_tool("terraform"):
        print(cs("this program will install terraform", "gold"))
    # error checking for both stop and start and no flags.
    if platform == "none":
        print(sysplat.system())
        print(sysplat.platform())
        print(sysplat.machine())
        print(os.name)
        print(sysplat.release())
        print(sysplat.version())
    else:
        print(platform)

if __name__ == "__main__":
    main()
