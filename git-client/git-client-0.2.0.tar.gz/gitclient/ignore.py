#!/usr/bin/env python

"""add or remove file from .gitignore"""

import os
import sys
import subprocess

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

COLORS = { 
    'CYAN': '\033[96m',
    'MAGENTA': '\033[95m',
    'GREY': '\033[90m',
    'LIGHTGREY': '\033[38;5;248m',
    'BLUE': '\033[94m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[33m',
    'RED': '\033[31m',
    'WARNING': '\033[93m',
    'FAIL': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
    'ORANGE': '\033[38;5;208m',
    'PINK': '\033[38;5;212m',
    'PALEYELLOW': '\033[38;5;228m',
    'PALEBLUE': '\033[38;5;111m',
    'GOLD': '\033[38;5;178m'
}
def cs(string, color):
    color_upper = color.upper()
    if color_upper not in COLORS:
        return string
    else:
        string = COLORS[color_upper]+string+COLORS['ENDC']
        return string

def ignore(ignores, yes=None, backup=None):
    """add or remove file from .gitignore"""
    changes = False
    try:
        git_root = subprocess.check_output("git rev-parse --show-toplevel", shell=True).decode("utf-8").strip()
        os.chdir(git_root)
    except:
        print(cs("You don't appear to be in a git repo.", "warning"))
        exit()
    if os.path.exists(git_root+"/.gitignore"):
        with open(git_root+"/.gitignore") as f:
            ignorefile_arr = f.readlines()
        ignorefile_arr = [x.strip() for x in ignorefile_arr]
    else:
        print(cs("No .gitignore found.", "paleyellow"))
        print(cs("Creating a new .gitignore", "green"))
        ignorefile_arr = []
    # loop sanitized list and add and remove items ass needed
    for r in ignores:
        if r in ignorefile_arr:
            if yes or query_yes_no("remove "+cs(r, "gold")+" from .gitignore?", default="yes"):
                ignorefile_arr.remove(r)
                changes = True
                print(cs(r, "fail"))
        else:
            ignorefile_arr.append(r)
            changes = True
            print(cs(r, "green"))
    # finally, backup and over-write editted array to ignore file
    if backup:
        backup_ignore = git_root+"/.gc.bak.gitignore"
        print(cs("backing up ignore file to: ", "paleblue")+cs(".gc.bak.gitignore", "paleyellow"))
        bcmd = "cp "+git_root+"/.gitignore "+git_root+"/.gc.bak.gitignore"
        subprocess.call(bcmd, shell=True)
    if changes:
        newif = ""
        print(cs("========", "grey"))
        print("over-writing .gitignore")
        for r in ignorefile_arr:
            newif += r+"\n"
        f = open(git_root+"/.gitignore", "w+")
        f.write(newif)
        f.close()

if __name__ == "__main__":
    ignore()
