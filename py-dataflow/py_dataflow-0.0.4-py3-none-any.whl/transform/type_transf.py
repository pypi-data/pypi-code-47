# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, json
from datetime import datetime



def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = str(nfkd_form.encode('ASCII', 'ignore'), 'utf-8')
    return only_ascii


"""
###########################################################################
                        convert float, numeric
###########################################################################
"""
def to_percent(value=0):
    """
    :param _value:
    :return:
    """
    if value != 0:
        return '{percent:.2%}'.format(percent= value)

def to_float(value=None):
    """
    :param value:
    :return:   price_attack = str(round(float(price_attack),2)).replace('.',',')
    """
    # if value[-1:] == "'":
    #   value = value[:-1]
    # if value.strip() == '-':
    #   return 0
    # value = float(str(value).replace('.','').replace(',','.').replace('%', '')) #[:-1]
    # return float("{0:.2f}".format(round(value,2)))
    # import ipdb; ipdb.set_trace()
    value = value or '0'
    if value[:1] == '+':
        return value.replace('+','')
    elif value.strip() == '-':
        return 0
    elif value[-1] == 'M':
        value = value.replace('M','00000').replace(',','')
    return float(str(value).replace('.','').replace(',','.'))
