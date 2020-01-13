#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys

try:
    from yoc import *
except:
    from yoctools.yoc import *

def usage():
    print("Usage:")
    print("  yoc <command> [options]\n")
    print("Commands:")
    print("  install                     Install component.")
    print("  uninstall                   Uninstall component.")
    print("  list                        List all packages")
    print("  update                      update all packages")
    print("  upload                      update all packages")
    print("  variable                    show variable")
    print("")

    print("General Options:")
    print("  -h, --help                  Show help.")


def main():
    argc = len(sys.argv)
    if argc < 2:
        usage()
        exit(0)

    if sys.argv[1] == 'list':
        yoc = YoC()
        yoc.occ_update()
        yoc.occ_components.show()
    elif sys.argv[1] == 'lo':
        yoc = YoC()
        yoc.list()
    elif sys.argv[1] in ['install', 'download']:
        if argc >= 3:
            yoc = YoC()
            yoc.add_component(sys.argv[2])
            yoc.update()
            print("%s download Success!" % sys.argv[2])
    elif sys.argv[1] in ['uninstall', 'remove']:
        if argc >= 3:
            yoc = YoC()
            if yoc.remove_component(sys.argv[2]):
                yoc.update()
                print("%s uninstall Success!" % sys.argv[2])
    elif sys.argv[1] == 'update':
        yoc = YoC()
        yoc.update()
    elif sys.argv[1] == 'upload':
        yoc = YoC()
        if argc >= 3:
            yoc.upload(sys.argv[2])
        if argc == 2:
            yoc.uploadall()

    elif sys.argv[1] == 'sdk':
        yoc = YoC()
        solution = yoc.getSolution()
        solution.install()

    elif sys.argv[1] == 'variable':
        yoc = YoC()
        solution = yoc.getSolution()
        if argc >= 3:
            var = solution.variables.get(sys.argv[2])
            print(var)
        else:
            for k, v in solution.variables.items():
                print("%-10s = %s" % (k, v))
    elif sys.argv[1] == 'show':
        yoc = YoC()
        solution = yoc.getSolution()
        solution.show()
        for c in solution.components:
            c.show()
            c.info(4)


if __name__ == "__main__":
    yoc = YoC()
    solution = yoc.getSolution()
    solution.show()
    for c in solution.components:
        c.show()
        c.info(4)
