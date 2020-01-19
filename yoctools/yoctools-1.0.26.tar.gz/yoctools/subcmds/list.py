# -*- coding:utf-8 -*-


import re
import sys

from yoctools import *

class List(Command):
    common = True
    helpSummary = "List component"
    helpUsage = """
%prog [-a] [<component>...]
"""
    helpDescription = """
List all projects; pass '.' to list the project for the cwd.
"""
    def _Options(self, p):
        p.add_option('-a', '--all',
                     dest='show_all', action='store_true',
                     help='show the complete list of commands')

    def Execute(self, opt, args):
        if opt.show_all:
            yoc = YoC()
            yoc.occ_update()
            yoc.occ_components.show()
        else:
            yoc = YoC()
            yoc.list()
