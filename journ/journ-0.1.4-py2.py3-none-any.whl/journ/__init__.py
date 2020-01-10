"""
/----------------------------------------------------\
|     journ v0.1.3 Copyright (c) 2020 Ron Becker     |
|----------------------------------------------------|
|                                                    |
|                                                    |
| journ is a command line journal program written in |
| Python. It saves all your journal entries in a     |
| text file called journ.txt in your home directory. |
|                                                    |
| To begin using journ after installing it just type |
| `journ` in terminal. A text input will appear and  |
| you can begin typing. After you are finished just  |
| hit enter. The new entry is automatically added to |
| the end of journ.py with the date and time.        |
|                                                    |
\----------------------------------------------------/
"""

import os
import subprocess
from time import gmtime, strftime
from pathlib import Path

# Some color. For me.
class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# This is how I get it to work with pip and console scripts.
# Is there an easier/better way? Please help. I'm still sorting
# my shit out!
def main():
    # A class, because I'm starting to like them way more than a bunch of variables.
    # I can't help it. Plus, it's a cleaner and more organized look in my opinion.
    class App:
        def __init__(self, filename, name, version, site, repo, devname, devemail, devsite):
            self.filename = filename
            self.name = name
            self.version = version
            self.site = site
            self.repo = repo
            self.devname = devname
            self.devemail = devemail
            self.devsite = devsite

    app = App('journ.txt', 'journ', 'v0.1.3', 'https://ronbecker.github.io/journ', 'https://github.com/ronbecker/journ', 'Ron Becker', 'ronbecker@linuxmail.org', 'https://ronbecker.github.io')

    # Set date and home folder varialbles
    today = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    home = str(Path.home())
    journ_file = home + "/" + app.filename

    # Title, and app info that appears over entry input.
    print("")
    print("           Welcome to " + app.name + " " + app.version + "           ")
    print("             Copyright (c) 2020              ")
    print("")
    print("   Site: " + app.site)
    print("   Repo: " + app.repo)
    print("")
    print("           Write your entry below.           ")
    print("")
    # This chunk opens journ.txt in the users home directory
    # takes their input, and appends it to journ.txt along
    # with the date and time, and a blank line so that each
    # entry is a little more readable.
    with open (journ_file, "a") as journ_entry:
        journ_entry.write (str(today) + ": \n")
        journ_entry.write (input("> "))
        journ_entry.write ("\n\n")
        print("")

def upgrade():
    subprocess.call(["pip3", "install", "--upgrade", "journ"])
    print("Finished running journ upgrade.")

def egg():
    print(colors.FAIL + colors.BOLD + "-------------------------------------------------------------" + colors.ENDC)
    print(" ")
    print(colors.FAIL +"Naughty John, Naughty John, does his work with his apron on." +colors.ENDC)
    print(colors.FAIL +"Cuts your throat and takes your bones, sells 'em off for a coupla stones." +colors.ENDC)
    print(" ")
    print(colors.FAIL + colors.BOLD + "-------------------------------------------------------------" + colors.ENDC)
