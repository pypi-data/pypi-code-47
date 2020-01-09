"""
/----------------------------------------------------\
|   journ.py v0.1.0 Copyright (c) 2020 Ron Becker    |
|  --------------------------------------------------|
|                  About journ.py                    |
|                                                    |
| jounr.py is a command line journal program written |
| in Python. It saves all your journal entries in a  |
| text file called journ.txt in the same directory   |
| as journ.py.                                       |
|                                                    |
| To begin using journ.py after installing it just   |
| type `journ` in terminal. A text input will appear |
| and you can begin typing. After you are finished   |
| just hit enter. The new entry is automatically     |
| added to the end of journ.py with the date and     |
| time of entry.                                     |
\----------------------------------------------------/
"""

import os
from time import gmtime, strftime
from pathlib import Path

# Add text colors and stuff. I may not use all of them, but I like to have them.
class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
     # Set date and home folder varialbles
     today = strftime("%Y-%m-%d %H:%M:%S", gmtime())
     home = str(Path.home())
     filename = 'journ.txt'
     journ_file = home + "/" + filename
     journ_check = os.path.isfile(journ_file)


     if journ_check == False:
         print(colors.BLUE + colors.BOLD + "-----------------------------------------------------" + colors.ENDC)
         print("")
         print(colors.BLUE + colors.BOLD + "It looks like this is your first time using journ.py!" + colors.ENDC)
         print(colors.BLUE + colors.BOLD + "You will be able to find your journal file at:       " + colors.ENDC)
         print("")
         print(colors.GREEN + colors.BOLD + "            " + journ_file + colors.ENDC)
         print("")
         print(colors.BLUE + colors.BOLD + "-----------------------------------------------------" + colors.ENDC)
         print("")
         input(colors.BLUE + colors.BOLD + "Press Enter to begin using journ.py..." + colors.ENDC)
         print("")

         with open(journ_file, "a") as journ_entry:
             journ_entry.write (str(today) + ": \n")
             journ_entry.write (input("> "))
             journ_entry.write ("\n\n")
             #Print a nice little confirmation message. Its even green.
             print(" ")
             print(colors.GREEN + "Entry added!" + colors.ENDC)

     elif journ_check == True:
         # This block opens journ.txt in the users home directory
         # takes their input, and appends it to journ.txt along
         # with the date and time, and a blank line so that each
         # entry is a little more readable.
         with open (journ_file, "a") as journ_entry:
             journ_entry.write (str(today) + ": \n")
             journ_entry.write (input("> "))
             journ_entry.write ("\n\n")
             #Print a nice little confirmation message. Its even green.
             print(" ")
             print(colors.GREEN + "Entry added!" + colors.ENDC)
