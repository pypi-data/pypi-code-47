#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/12/20 15:45
# @Author  : Niyoufa
import hashlib


def md5(mingwen):
    """MD5"""
    m = hashlib.md5()
    mdr_str = mingwen.encode()
    m.update(mdr_str)
    ciphertext = m.hexdigest()
    return ciphertext
