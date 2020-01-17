'''
Created on 28 janv. 2019

@author: jeanluc
'''
import sys

from os.path import expanduser

def run(argv):
    home = expanduser("~")
    light = len(argv) and argv[0]

if __name__ == '__main__':
    run(sys.argv[1:])