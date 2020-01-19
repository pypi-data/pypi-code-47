#!/usr/bin/env python
# -*- coding: cp65001 -*-
from __future__ import print_function

# Here, I'd like to apologize to whoever is reading this source code,
# It might be painful for you the reader to read through this if you're
# a programmer, this includes bad programming practices.
# And you might see some poor documentation. Sorry.
# -- Supernova, 1.19.2020 4:39 PM
#
# And also, the whole point of overcomplicating Python is f**king defeated
# When you do from overpython import *!
# -- Supernova, 1.19.2020 4:41 PM

import sys, os
import string, math
import time, datetime
from sys import platform as pt_
import platform

__version__     = "1.1.1"
__warename__    = "Overcomplicated Python (Overpython)"
ascii_letters   = string.ascii_letters
numbers         = string.digits
variables       = {}
PI              = math.pi
EULER           = math.e

class NoArguments(Exception):
    pass

def getchr(character):
    return chr(character)

def getord(character):
    return ord(character)

def machine():
    """
    overpython.machine()

    Returns current machine name.
    """
    return platform.platform()

def new_variable(type_, name, value):
    """
    overpython.new_variable(type_, name, value)

    Create a new variable. Overpython will then store it in a dictionary.
    You can access it by doing "overpython.variables["name here"]
    """
    global variables
    if type_ == "universal":
        variables[name] = value
    elif type_ == "boolean":
        if value == True or value == False:
            variables[name] = value
        else:
            raise ValueError("%s is not True or False" % name)
    elif type_ == "string":
        variables[name] = str(value)
    elif type_ == "int":
        try:
            variables[name] = int(value)
        except ValueError:
            raise ValueError("%s is not an integer" % name)
    elif type_ == "float":
        try:
            variables[name] = float(value)
        except ValueError:
            raise ValueError("%s is not a float" % name)
    else:
        raise NoArguments("No arguments provided")

def printnl(text):
    """
    overpython.printnl(text)

    Print without a line break.
    """
    sys.stdout.write(text)

def println(text):
    """
    overpython.println(text)

    Print with a line break.
    """
    print(text)

def get(text=""):
    """
    overpython.get(text="")

    Get user input from console.
    """
    return input(text)

def help():
    print(f"{__warename__} {__version__}")
    print(f"The one package that overcomplicates Python! Yay!")

def version():
    return __version__

def pause():
    """
    overpython.pause()

    Will ask the user to press ENTER key and exits with code 64.
    overpython.returnf(0) will also do the same exact function.
    """
    print("Press the ENTER key to exit...")
    input()
    exit(64)

def fileExists(filename):
    """
    overpython.fileExists(filename)

    Check if a file exists. Will return False if it does not exist.
    Otherwise, it will return True if it does exist.
    """
    return os.path.exists(filename)

def isAccesible(path, mode='r'):
    """
    overpython.isAccessible(path, mode='r')
    
    Check if the file or directory at `path` can
    be accessed by the program using `mode` open flags.
    """
    try:
        f = open(path, mode)
        f.close()
    except IOError:
        return False
    return True

def newFile(filename, content=""):
    """
    overpython.newFile(filename, content="")
    
    Create a new file, if no content is provided. Then it'll create the file
    without any content. Raises FileExistsError if it exists.

    On the other hand, if the file exists and the content argument is not "",
    then it'll automatically overwrite that file.
    """
    if content == "":
        try:
            f = open(filename, "x")
            f.close()
        except FileExistsError:
           raise FileExistsError("File already exists (%s)" % filename)
    else:
        f = open(filename, "w+")
        f.write(content)
        f.close()

def split(char: str, source: str):
    """
    overpython.split(char: str, source: str)
    
    Is the same thing as string.split()
    .split() 101:
        - will split up source at char into a list
        - found that confusing? internet!
    """
    try:
        return source.split(char)
    except ValueError:
        raise ValueError("%s is not a string" % name)

def startsWith(keyword: str, source: str):
    """
    overpython.startsWith(keyword: str, source: str)
    
    Check if source starts with keyword. Returns True if it does.
    Otherwise, it'll return False.
    """
    try:
        return source.startswith(char)
    except ValueError:
        raise ValueError("%s is not a string" % name)

def endsWith(keyword: str, source: str):
    """
    overpython.endsWith(keyword: str, source: str)
    
    Check if source starts with keyword. Returns True if it does.
    Otherwise, it'll return False.
    """
    try:
        return source.endswith(char)
    except ValueError:
        raise ValueError("%s is not a string" % name)

def add(intf, ints):
    """
    overpython.add(intf, ints)
    
    Add intf with ints. Raises ValueError if intf/ints is a string.
    """
    try:
        return float(intf) + float(ints)
    except ValueError:
        raise ValueError("%s/%s is not a number" % (intf, ints))

def clearscreen():
    """
    overpython.clearscreen()
    
    Clear the screen.
    """
    if pt_.startswith("win"):
        os.system("cls")
    elif pt_.startswith("linux") or pt_ == "darwin":
        os.system("clear")
    else:
        return "N/A"

def cls():
    """
    overpython.cls()
    
    Alias of overpython.clearscreen()
    """
    clearscreen()

def clr():
    """
    overpython.clr()
    
    Alias of overpython.clearscreen()
    """
    clearscreen()

def clear():
    """
    overpython.clear()
    
    Alias of overpython.clearscreen()
    """
    clearscreen()
    
def returnf(value):
    """
    overpython.returnf(value)
    
    Does the same function as the return statement. If 0 is the value,
    then it'll automatically execute overpython.pause()
    """
    if value == 0:
        pause()
    else:
        return f"{value}"

def wait(seconds):
    """
    overpython.wait(seconds)
    
    Wait `seconds` seconds. (repetition, eh?)
    """
    try:
        time.sleep(int(seconds))
    except Exception as e:
        print(e)

def subt(intf, ints):
    """
    overpython.subt(intf, ints)
    
    Subtract intf with ints. Raises ValueError if intf/ints is a string.
    """
    try:
        return float(intf) - float(ints)
    except ValueError:
        raise ValueError("%s/%s is not a number" % (intf, ints))

def multiply(intf, ints):
    """
    overpython.multiply(intf, ints)
    
    Multiply intf by ints. Raises ValueError if intf/ints is a string.
    """
    try:
        return float(intf) * float(ints)
    except ValueError:
        raise ValueError("%s/%s is not a number" % (intf, ints))

def include(name, root_package=False, relative_globals=None, level=0):
    """
    overpython.include(name, root_package=False, relative_globals=None, level=0)
    
    Imports a module. Acts very much like the import statement.
    If the module name given is not found, Python automatically raises ImportError.
    """
    return __import__(name, locals=None, # locals has no use
                      globals=relative_globals, 
                      fromlist=[] if root_package else [None],
                      level=level)
    
def divide(intf, ints):
    """
    overpython.divide(intf, ints)
    
    Divide intf by ints. Raises ValueError if intf/ints is a string.
    """
    try:
        return float(intf) / float(ints)
    except ValueError:
        raise ValueError("%s/%s is not a number" % (intf, ints))

def modulus(intf, ints):
    """
    overpython.modulus(intf, ints)
    
    Calculate the modulus of intf and ints. Raises ValueError if intf/ints is a string.
    """
    try:
        return float(intf) % float(ints)
    except ValueError:
        raise ValueError("%s/%s is not a number" % (intf, ints))

"""
Source: http://www.montypython.net/scripts/cheese.php

AND NOW... CHEESE

(a customer walks in the door.)
Customer (John Cleese): Good Morning.
Owner (Michael Palin): Good morning, Sir. Welcome to the National Cheese Emporium!
Customer: Ah thank you my good man.
Owner: What can I do for you, Sir?
C: Well, I was, uh, sitting in the public library on Thurmon Street just now, skimming through 'Rogue Herrys' by Hugh Walpole, and I suddenly came over all peckish.
O: Peckish, sir?
C: Esuriant.
O: Eh?
C: 'Ee I were all 'ungry-like!
O: Ah, hungry!
C: In a nutshell. And I thought to myself, 'a little fermented curd will do the trick', so, I curtailed my Walpoling activites, sallied forth, and infiltrated your place of purveyance to negotiate the vending of some cheesy comestibles!
O: Come again?
C: I want to buy some cheese.
O: Oh, I thought you were complaining about the bouzouki player!
C: Oh, heaven forbid: I am one who delights in all manifestations of the Terpsichorean muse!
O: Sorry?
C: 'Ooo, Ah lahk a nice tune, 'yer forced to!
O: So he can go on playing, can he?
C: Most certainly! Now then, some cheese please, my good man.
O: (lustily) Certainly, sir. What would you like?
C: Well, eh, how about a little Red Leicester.
O: I'm, a-fraid we're fresh out of Red Leicester, sir.
C: Oh, never mind, how are you on Tilsit?
O: I'm afraid we never have that at the end of the week, sir, we get it fresh on Monday.
C: Tish tish. No matter. Well, stout yeoman, four ounces of Caerphilly, if you please.
O: Ah! It's beeeen on order, sir, for two weeks. Was expecting it this morning.
C: 'T's Not my lucky day, is it? Aah, Bel Paese?
O: Sorry, sir.
C: Red Windsor?
O: Normally, sir, yes. Today the van broke down.
C: Ah. Stilton?
O: Sorry.
C: Gruyere? Emmental?
O: No.
C: Any Norwegian Jarlsberger, per chance?
O: No.
C: Liptauer?
O: No.
C: Lancashire?
O: No.
C: White Stilton?
O: No.
C: Danish Blue?
O: No.
C: Double Gloucester?
O: (pause) No.
C: Cheshire?
O: No.
C: Dorset Blue Vinney?
O: No.
C: Brie, Roquefort, Pont-l'Eveque, Port Salut, Savoyard, Saint-Paulin, Carre-de-L'Est, Boursin, Bresse Bleu, Perle de Champagne?
O: No.
C: Camembert, perhaps?
O: Ah! We have Camembert, yessir.
C: (suprised) You do! Excellent.
O: Yessir. It's ah... it's a bit runny.
C: Oh, I like it runny.
O: Well,.. It's very runny, actually, sir.
C: No matter. Fetch hither the fromage de la Belle France! Mmmwah!
O: I...think it's a bit runnier than you'll like it, sir.
C: I don't care how f**king runny it is. Hand it over with all speed.
O: Oooooooooohhh........! (pause)
C: What now?
O: The cat's eaten it.
C: (pause) Has he?
O: She, sir.
(pause)
C: Gouda?
O: No.
C: Edam?
O: No.
C: Caithness?
O: No.
C: Smoked Austrian?
O: No.
C: Japanese Sage Darby?
O: No sir.
C: You... do have some cheese, don't you?
O: (brightly) Of course, sir. It's a cheese shop, sir. We've got-
C: No no... don't tell me. I'm keen to guess.
O: Fair enough.
C: Uuuuuh, Wensleydale.
O: Yes?
C: Ah, well, I'll have some of that!
O: Oh! I thought you were talking to me, sir. Mister Wensleydale, that's my name.
(pause)
C: Greek Feta?
O: Uh, not as such.
C: Uuh, Gorgonzola?
O: No
C: Parmesan?
O: No
C: Mozzarella?
O: No
C: Pippo Creme?
O: No
C: Danish Fimboe?
O: No
C: Czech sheep's milk?
O: No
C: Venezuelan Beaver Cheese?
O: Not -today-, sir, no.
(pause)
C: Aah, how about Cheddar?
O: Well, we don't get much call for it around here, sir.
C: Not much ca--It's the single most popular cheese in the world!
O: Not 'round here, sir.
C: (slight pause) and what IS the most popular cheese 'round hyah?
O: 'Illchester, sir.
C: IS it.
O: Oh, yes, it's staggeringly popular in this manusquire.
C: Is it.
O: It's our number one best seller, sir!
C: I see. Uuh... 'Illchester, eh?
O: Right, sir.
C: All right. Okay. 'Have you got any?' He asked, expecting the answer 'no'.
O: I'll have a look, sir.. nnnnnnnnnnnnnnnno.
C: It's not much of a cheese shop, is it?
O: Finest in the district sir!
C: (annoyed) Explain the logic underlying that conclusion, please.
O: Well, it's so clean, sir!
C: It's certainly uncontaminated by cheese.
O: (brightly) You haven't asked me about Limburger, sir.
C: Would it be worth it?
O: Could be.
C: Have you --SHUT THAT BLOODY BOUZOUKI OFF!
O: Told you sir...
C: (slowly) Have you got any Limburger?
O: No.
C: Figures. Predictable, really I suppose. It was an act of purest optimism to have posed the question in the first place....... Tell me:
O: Yessir?
C: (deliberately) Have you in fact got any cheese here at all?
O: Yes,sir.
C: Really?
(pause)
O: No. Not really, sir.
C: You haven't.
O: Nosir. Not a scrap. I was deliberately wasting your time,sir.
C: Well I'm sorry, but I'm going to have to shoot you.
O: Right-0, sir.
(The customer takes out a gun and shoots the shopkeeper)
C: What a senseless waste of human life.
"""
