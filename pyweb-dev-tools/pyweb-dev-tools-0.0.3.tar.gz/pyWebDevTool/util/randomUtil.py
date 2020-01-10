# -*- coding: utf-8 -*-
import random


def random_str(length=18):
    return "".join(random.sample('zyxwvutsrqponmlkjihgfedcba', length))


def random_number(length=18):
    return ''.join(str(random.choice(range(length))) for _ in range(length))
