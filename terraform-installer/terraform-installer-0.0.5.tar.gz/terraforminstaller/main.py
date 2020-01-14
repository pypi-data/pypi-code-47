#!/usr/bin/env python

"""install or update to the latest version of terraform open source version"""

import argparse
from argparse import RawTextHelpFormatter as rawtxt
import sys
import signal
import json
import os
import time
import platform as sysplat
import subprocess
import pkg_resources
from stringcolor import *
from bs4 import BeautifulSoup
import requests
import numpy as np
from functools import reduce

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
    try:
        response = requests.get(website).text
    except Exception:
        print(cs("SORRY", "red", "lightgrey6")+cs(" cannot get terraform releases.", "yellow"))
        print(cs("please check your internet connection and try again.", "lightgoldenrod"))
        exit()
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
    try:
        response = requests.get(website).text
    except Exception:
        print(cs("SORRY", "red", "lightgrey6")+cs(" cannot get terraform releases.", "yellow"))
        print(cs("please check your internet connection and try again.", "lightgoldenrod"))
        exit()
    soup = BeautifulSoup(response, 'html.parser')
    platforms = []
    for list_item in soup.find_all('li'):
        if list_item.contents[1].contents[0] != "../" and list_item.contents[1].contents[0] != f'terraform_{version}_SHA256SUMS' and list_item.contents[1].contents[0] != f'terraform_{version}_SHA256SUMS.sig':
            platforms.append(list_item.contents[1].contents[0].replace(f"terraform_{version}_", "").replace(".zip", ""))
    return platforms

def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return "The strings are {} edits away".format(distance[row][col])

def highest_levenshtein_ratio(platform, release):
    """find the closest match given platform, and release"""
    plat_sniff = platform.split("-")
    results = []
    contenders = []
    for p in get_platforms(release):
        total_distance = 0
        for sniff in plat_sniff:
            ratio = levenshtein_ratio_and_distance(p.split("_")[0] ,sniff, ratio_calc = True)
            if ratio > .7:
                contenders.append(p)
            ratio = levenshtein_ratio_and_distance(p, sniff, ratio_calc = True)
            total_distance = total_distance + ratio
        results.append({"distance":total_distance, "platform":p})
    if len(contenders) == 1:
        return contenders[0]
    else:
        best = 0
        best_match = {}
        for r in results:
            if r["platform"] in contenders:
                if r["distance"] > best:
                    best = r["distance"]
                    best_match = {"distance":r["distance"], "platform":r["platform"]}
        return best_match["platform"]

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
        help="""$ ti linux_amd64\n
options are """+str(get_platforms(get_versions(first=True))),
        nargs='?',
        default='none'
    )
    parser.add_argument('-r', '--release', help=f"install a specific release. default={get_versions(first=True)}", default=get_versions(first=True))
    parser.add_argument('-y', '--yes', action='store_true', help='approve all prompts as yes.')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s '+version)
    args = parser.parse_args()
    platform = args.platform
    release = args.release
    yes = args.yes
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
        use_term = ["install", "installing"]
    else:                                                                                                           
        print(cs("terraform found", "lightgreen"), cs("this program will update terraform to", "gold"), cs(release, "steelblue2"))
        use_term = ["update to", "updating to"]

    if platform == "none":
        print(cs("no platform provided. attempting to sniff...", "grey"))
        print(cs("platform found:", "grey"), cs(sysplat.platform(), "lightgoldenrod"))
        best_match = highest_levenshtein_ratio(sysplat.platform(), release)
        print(cs(best_match, "sandybrown"), cs("seems like the closest match", "lightgrey3"))
        if yes or query_yes_no(f"{use_term[0]} terraform {release}?", "yes"):
            print()
            time.sleep(1)
            print(cs(f"{use_term[1]} terraform {release}...", "pink"))
            print("please note: this program is in beta and is not yet functional")
    else:
        if yes or query_yes_no(f"{use_term[0]} terraform {release}?", "yes"):
            print()
            time.sleep(1)
            print(cs(f"{use_term[1]} terraform {release}...", "pink"))
            print("please note: this program is in beta and is not yet functional")

if __name__ == "__main__":
    main()
