#!/usr/bin/env python

"""install or update to the latest version of terraform open source version"""

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
from bs4 import BeautifulSoup
import requests

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

def get_versions(first=None):
    """get versions of terraform from the website"""
    website = "https://releases.hashicorp.com/terraform/"
    response = requests.get(website).text
    soup = BeautifulSoup(response, 'html.parser')
    versions = []
    for list_item in soup.find_all('li'):
        if list_item.contents[1].contents[0] != "../":
            versions.append(list_item.contents[1].contents[0])
    if first is None:
        return versions
    else:
        return versions[0].replace("terraform_", "")

def get_platforms(version):
    """get platforms for version"""
    website = f"https://releases.hashicorp.com/terraform/{version}/"
    response = requests.get(website).text
    soup = BeautifulSoup(response, 'html.parser')
    platforms = []
    for list_item in soup.find_all('li'):
        if list_item.contents[1].contents[0] != "../" and list_item.contents[1].contents[0] != f'terraform_{version}_SHA256SUMS' and list_item.contents[1].contents[0] != f'terraform_{version}_SHA256SUMS.sig':
            platforms.append(list_item.contents[1].contents[0].replace(f"terraform_{version}_", "").replace(".zip", ""))
    return platforms

def main():
    '''install or update to the latest version of terraform'''
    version = pkg_resources.require("terraform-installer")[0].version
#    version = "0.0.0"
    parser = argparse.ArgumentParser(
        description='install or update to the latest version of terraform open source version',
        formatter_class=rawtxt
    )

    #parser.print_help()
    parser.add_argument(
        "platform",
        help=""".\n\n
    $ ti linux_amd64\n
    options are """+str(get_platforms(get_versions(first=True))),
        nargs='?',
        default='none'
    )
    parser.add_argument('-r', '--release', help=f"install a specific release. default={get_versions(first=True)}", default=get_versions(first=True))
#    parser.add_argument('-g', '--green', action='store_true', help='start.')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s '+version)
    args = parser.parse_args()
    platform = args.platform
    release = args.release
    all_versions = get_versions()
    # error check for release existing
    if "terraform_"+release not in all_versions:
        print(cs("SORRY", "red", "lightgrey6")+cs(" can't find the release: ", "yellow")+cs(release, "red"))
        print(cs("available versions:", "grey"))
        print(str([version.replace("terraform_", "") for version in all_versions]))
        exit()

    # check that release version includes platform
    if platform != "none":
        if platform not in get_platforms(release):
            print(cs("SORRY", "red", "lightgrey6")+cs(f" can't find the platform: {cs(platform, 'red')}", "yellow")+cs(f" in version {cs(release, 'red')}", "yellow"))
            print(cs("available platforms:", "grey"))
            print(str(get_platforms(release)))

    print(bytes.decode(b'\xF0\x9F\x9A\xA7', 'utf8')+" work in progress. version: {} ".format(version)+bytes.decode(b'\xF0\x9F\x9A\xA7', 'utf8'))

    # check for terraform
    if not is_tool("terraform"):
        print(cs("this program will install terraform", "gold"))

    if platform == "none":
        print("no platform provided. attempting to sniff...")
        print(sysplat.platform())
        print()
        print(release)
        print(get_platforms(release))
    else:
        print(platform)

if __name__ == "__main__":
    main()
