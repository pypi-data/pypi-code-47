'''
Created on Jan 8, 2020

@author: jeanluc
'''
import sys,os
from string import Template
from _ast import arg

def translate(text, dico):
    s = Template(text)
    res = s.substitute(dico)
    return res

def dotranslate(source, target, dico):
    res = ""
    if os.path.exists(source):
        with open(source, "r") as ff:
            text = ff.read()
            res = translate(text, dico)
            try:
                if os.path.exists(target):
                    os.remove(target)
                with open(target, "w") as ft:
                    ft.write(res)
            except: pass
    return res
    
if __name__ == '__main__':
    dico = {}
    for ind, arg in enumerate(sys.argv[3:]):
        if not ind % 2:
            mem = arg
        else:
            dico[mem] = arg
    dotranslate(sys.argv[1], sys.argv[2], dico)
    print("translate {} with {}".format(sys.argv[1], dico))
    print('done')