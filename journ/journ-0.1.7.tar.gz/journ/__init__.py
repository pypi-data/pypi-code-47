"""
#---------------------------------------------------#
     journ v0.1.7 Copyright (c) 2020 Ron Becker
#---------------------------------------------------#


 journ is a command line journal program written in
 Python. It saves all your journal entries in a
 text file called journ.txt in your home directory.

 To begin using journ after installing it just type
 `journ` in terminal. A text input will appear and
 you can begin typing. After you are finished just
 hit enter. The new entry is automatically added to
 the end of journ.py with the date and time.

#---------------------------------------------------#
"""
import os
from time import gmtime, strftime
from pathlib import Path
def main():
    class App:
        def __init__(self, name, version, site, repo):
            self.name = name
            self.version = version
            self.site = site
            self.repo = repo
    # Class vairable to make changing things easier for me.
    # And because I like them.
    app = App('journ', 'v0.1.7', 'https://ronbecker.github.io/journ', 'https://github.com/ronbecker/journ')
    # Set date, home folder, and file name varialbles.
    today = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    home = str(Path.home())
    journ_file = home + "/journ.txt"
    # Welcome Information and User input
    print("")
    print("           Welcome to ", app.name, app.version)
    print("             Copyright (c) 2020\n\n")
    print("   Repo: ", app.repo)
    print("")
    # Opens journ.txt if it exitsts, and if not it creates it. And
    # appends the user input to the file. Along with the date and
    # time of entry, and a blank line at the end for readablity.
    with open (journ_file, "a") as journ_entry:
        journ_entry.write (str(today) + ": \n")
        journ_entry.write (input("> "))
        journ_entry.write ("\n\n")
        print("")
