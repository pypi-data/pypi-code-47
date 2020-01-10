# -*- coding: utf-8 -*-


def like_key(dic, key, str):
    if key in dic.keys() and str in dic[key]:
        return True
    return False


def get_value(dic, key):
    if dic is None:
        return None
    if key in dic.keys():
        return dic[key]
    return None
