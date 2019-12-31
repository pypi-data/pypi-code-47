#!/usr/bin/env python

"""CLI git client"""

import argparse
from argparse import RawTextHelpFormatter
import sys
import os
import signal
import time

def signal_handler(sig, frame):
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

class Bcolors:
    """console colors"""
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    GREY = '\033[90m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ORANGE = '\033[38;5;208m'
    PINK = '\033[38;5;212m'
    PALEYELLOW = '\033[38;5;228m'
    PALEBLUE = '\033[38;5;111m'
    GOLD = '\033[38;5;178m'

def main():
    """git clienting"""
    parser = argparse.ArgumentParser(description='simple usable git client', prog='gc', formatter_class=RawTextHelpFormatter)

    #parser.print_help()
    parser.add_argument("message", help="the message you want to commit with.\n\nexample: $ gc added state var to file.js", nargs='+')
    version = pkg_resources.require("spin-and-heave")[0].version
    parser.add_argument('-v', '--version', action='version', version='%(prog)s '+version)
    final = bytes.decode(b'\xF0\x9F\x9A\xA7', 'utf8')+Bcolors.PALEYELLOW+" under construction. version: {} ".format(version)+Bcolors.ENDC+bytes.decode(b'\xF0\x9F\x9A\xA7', 'utf8')
    print(final)
    args = parser.parse_args()
    parser.print_help()
    exit()



    message = ""
    for item in args.message:
        message += item+" "
    os.system("git status")
    if query_yes_no("continue gitting?", "yes"):
        fullcmd = "git commit -a -m \""+message+"\""
        if query_yes_no("add files?"):
            os.system("git add --all")
        print("committing...")
        time.sleep(1)
        os.system(fullcmd)
        print("pushing...")
        time.sleep(1)
        os.system("git push")

if __name__ == "__main__":
    main()
