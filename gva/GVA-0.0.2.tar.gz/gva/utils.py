from random import getrandbits, choice


def get_random_id():
    return getrandbits(31) * choice([1, -1])
