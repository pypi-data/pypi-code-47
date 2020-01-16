#!/usr/bin/env python3
# coding: utf-8

import sys

from joker.superuser.main import registry

registry(['python3 -m joker.superuser'] + sys.argv[1:])
