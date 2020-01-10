#!/usr/bin/env python3
import os
from ezutils.files import readlines


def brother_path(file_name):
    return os.path.join(os.path.abspath(
        os.path.dirname(__file__)), file_name)


def print_using():
    lines = readlines(brother_path("./using.txt"))
    for line in lines:
        print(line)
