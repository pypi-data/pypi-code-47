#!/usr/bin/env python3
# coding: utf-8

from __future__ import unicode_literals, print_function


def chunkwize_parallel(chunksize, *args):
    import itertools
    # args are strings or lists
    chunksize = int(chunksize)
    for i in itertools.count(0):
        r = [s[i * chunksize:(i + 1) * chunksize] for s in args]
        if any(r):
            yield r
        else:
            break


def locate_submat(name):
    import os
    import joker.aligner

    d = os.path.split(joker.aligner.__file__)[0]
    possible_paths = [
        os.path.join(d, 'matrix', 'bioinfo', name),
        os.path.join(d, 'matrix', name),
        name,
    ]

    for p in possible_paths:
        if os.path.isfile(p):
            return p
    errmsg = 'cannot find substitue matrix "{}"'.format(name)
    raise IOError(errmsg)


def load_submat(path):
    import numpy

    if '/' not in path:
        path = locate_submat(path)

    with open(path) as infile:
        ichars = []
        jstr = None
        jsize = 0
        scores = []

        for line in infile:
            line = line.strip()
            if line and not line.startswith('#'):
                # remove whitespaces
                jstr = ''.join(line.split())
                jsize = len(jstr) + 1
                break

        if jstr is None:
            raise ValueError('bad substitution matrix')

        for line in infile:
            items = line.split()
            if not items:
                continue

            if len(items) != jsize:
                raise ValueError('bad substitution matrix')
            ichars.append(items[0])
            scores.append([int(s) for s in items[1:]])

    istr = ''.join(ichars)
    submat = numpy.array(scores, dtype=int)
    return istr, jstr, submat
