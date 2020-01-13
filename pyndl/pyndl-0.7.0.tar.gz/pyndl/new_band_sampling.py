# !/usr/bin/env/python3
# coding: utf-8

import multiprocessing
import collections
import os
import random
import count


def preselected_items_bandsample(population_file,
                                 key_file,
                                 sample_size=50000,
                                 *,
                                 cutoff=5,
                                 seed=None,
                                 verbose=False):
    """
    Preselects outcomes and updates relevant files.

    """
    population = count.load_counter(population_file)
    key_list = [line.strip() for line in open(key_file, 'rt')]

    # make a copy of the population
    # filter all words that are in the list of preselected items
    selected = list()
    remained = list()
    for word, freq in population.items():
        if word in key_list:
            selected.append((word, freq))
        elif freq >= cutoff:
            remained.append((word, freq))

    # adjust sample size
    sample_size -= len(selected)

    # shuffle words with same frequency
    rand = random.Random(seed)  # TODO not working properly :(
    rand.shuffle(remained)
    remained.sort(key=lambda x: x[1])  # lowest -> highest freq

    step = sum(freq for word, freq in remained) / sample_size
    if verbose:
        print("step %.2f" % step)

    accumulator = 0
    index = 0
    sample = list()
    while 0 <= index < len(remained):
        word, freq = remained[index]
        accumulator += freq
        if verbose:
            print("%s\t%i\t%.2f" % (word, freq, accumulator))
        if accumulator >= step:
            sample.append((word, freq))
            accumulator -= step
            if verbose:
                print("add\t%s\t%.2f" % (word, accumulator))
            del remained[index]
            while accumulator >= step and index >= 1:
                index -= 1
                sample.append(remained[index])
                accumulator -= step
                if verbose:
                    word, freq = remained[index]
                    print("  add\t%s\t%.2f" % (word, accumulator))
                del remained[index]
        else:
            # only add to index if no element was removed
            # if element was removed, index points at next element already
            index += 1
            if verbose and index % 1000 == 0:
                print(".", end="")
                sys.stdout.flush()
    sample.extend(selected)
    sample = collections.Counter({key: value for key, value in sample})
    return sample
