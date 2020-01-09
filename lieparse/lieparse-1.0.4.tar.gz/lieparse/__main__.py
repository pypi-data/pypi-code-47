#! /usr/bin/env python3
"""It is a part fron lieparse package
© 2019-2020 Vidmantas Balčytis
"""

from os import path
import re

version = "Unknown"
ver = re.compile(":Version:\s*(.*?)\s+")
here = path.abspath(path.join(path.dirname(__file__), ".."))
with open(path.join(here, 'README.rst'), encoding = "utf-8") as f:
    for l in f:
        m = ver.match(l)
        if m is not None:
            version = m.group(1)
            break
print("lieparse library version {}".format(version))
