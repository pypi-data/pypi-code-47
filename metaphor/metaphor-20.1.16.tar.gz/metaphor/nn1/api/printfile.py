'''
Created on 10 févr. 2019

@author: jeanluc
'''
import os, sys

from ._api_service import getVersionList
from ...nntoolbox.excelutils import getVbaProjectBin

def printInfo(subject='', caller=0):
    lst = getinfolist(subject, caller)
    for val in lst:
        print(val)

def getinfolist(subject='', caller=0):
    subject = subject.lower()
    result = []
    basedir = os.path.expanduser(chr(126))
    if not caller:
        basedir = os.path.join(basedir, "docker")
    if subject == 'help':
        if caller == 2:
            filename = "help/helplight.txt"
        else:
        #if caller == 2:
            filename = "help/help.txt"
        with open(os.path.join(basedir, filename), "r") as ff:
            st = ff.read().strip()
            result = [st]
    elif subject == 'license':
        with open(os.path.join(basedir, "LICENSE"), "r") as ff:
            st = ff.read().strip()
            result = [st]
    elif subject == 'description':
        with open(os.path.join(basedir, "README.txt"), "r") as ff:
            st = ff.read().strip()
            result = [st]
    elif subject == 'version':
        result = []
        with open(os.path.join(basedir, "version.txt"), "r") as ff:
            st = ff.read().strip()
            result.append("docker image : {0}".format(st))
        result.extend(getVersionList())   
    elif subject == 'env':
        result = []
        for key, val in os.environ.items(): 
            result.append("environ[{0}] = {1}".format(key, val))        
    elif subject == "vba":
        st = getVbaProjectBin()
        result = [st]
    return result
        
if __name__ == '__main__':
    action = 'version' if len(sys.argv) < 2 else sys.argv[1]
    printInfo(action)
    