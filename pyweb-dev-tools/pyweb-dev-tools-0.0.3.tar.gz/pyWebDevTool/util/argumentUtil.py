#!/usr/bin/env python
# coding=utf8
import sys


def is_dev():
    return has_sys_arg("-p=dev")


def is_exe():
    if sys.argv[0].endswith(".exe"):
        return True
    return False


def has_sys_arg(arg_name):
    for arg in sys.argv:
        if arg_name == arg:
            return True
    return False
