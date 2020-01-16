#!/usr/bin/env python3
# coding: utf-8

from __future__ import print_function

import os
import subprocess
import sys


def install(*packages):
    subprocess.run([sys.executable, '-m', 'pip'] + list(packages))


def gettext_pipconf(repo='https://pypi.org/simple/'):
    if not repo.startswith('https:'):
        repo = "https://" + repo + '/simple/'
    lines = ["[global]", "index-url = {}".format(repo)]
    return os.linesep.join(lines)
