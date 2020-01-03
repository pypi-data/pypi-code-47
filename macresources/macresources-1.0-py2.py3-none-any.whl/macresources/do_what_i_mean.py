#!/usr/bin/env python3

from .main import parse_rez_code, parse_file, make_rez_code, make_file

REZ_EXTENSIONS = ('.rdump', '.r')

def read(path):
    with open(path, 'rb') as f:
        data = f.read()

    if path.endswith(REZ_EXTENSIONS):
        return parse_rez_code(data)
    else:
        return parse_file(data)

def write(path, resources):
    if path.endswith(REZ_EXTENSIONS):
        data = make_rez_code(resources)
    else:
        data = make_file(resources)

    with open(path, 'wb') as f:
        f.write(data)
