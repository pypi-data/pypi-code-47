#Spitzer/chache folder
#this is for temporary files used by the program
#(will be cleared after the program is done)

import os

from Spitzer.print import print_error

path = __file__[:-9]

def create_file(name, content=''):
    file = open(path + name, 'a+')
    file.write(content)

def read_file(name):
    try:
        return open(path + name, 'r').read()
    except OSError as e:
        print_error(e.strerror)
        return ''

def remove_file(name):
    try:
        os.remove(path + name)
    except:
        pass

def clear(): #clears Spitzer/chache on exit
    for file in os.listdir(path):
        if not file.endswith('.py') and not file.startswith('__pycache__'):
            os.remove(path + file)

def get_path():
    return path