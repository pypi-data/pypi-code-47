# -*- coding:utf-8 -*-


import re
import sys

from yoctools import *

class Install(Command):
    common = True
    helpSummary = "Install component into project environment"
    helpUsage = """
%prog [<component>...]
"""
    helpDescription = """
Install component into project environment
"""
    # def _Options(self, p):
    #     p.add_option('-a', '--all',
    #                  dest='show_all', action='store_true',
    #                  help='show the complete list of commands')

    def Execute(self, opt, args):
        if len(args) > 0:
            yoc = YoC()
            for name in args:
                yoc.download_component(name)
                yoc.update()
                print("%s download done." % sys.argv[2])

