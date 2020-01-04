import collections


def isiter(arg, allow_dict=True, allow_str=False):
    if not isinstance(arg, collections.Iterable):
        return False
    elif type(arg) is str and not allow_str:
        return False
    elif type(arg) is dict and not allow_dict:
        return False
    else:
        return True
