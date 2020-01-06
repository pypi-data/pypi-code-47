#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Seaky
# @Date:   2019/8/20 14:57

import re


def comma_digit(s, tp=int):
    if str_is_number(s, tp, exp=True):
        return '{:,}'.format(int(s))
    return s


def str_is_number(s, tp=None, exp=True):
    '''

    :param s:
    :param tp: 指定int/float，None两者都行
    :param exp: 扩展，如果s是int/float，也可以返回true
    :return:
    '''
    if not isinstance(s, str):
        if exp and isinstance(s, int) and tp in (None, int):
            return True
        if exp and isinstance(s, float) and tp in (None, float):
            return True
        return False
    if tp == int:
        return re.match('^\d+\.{0,0}\d+$', s)
    elif tp == float:
        return re.match('^\d+\.{1,1}\d+$', s)
    else:
        return re.match('^\d+\.{,1}\d+$', s)


def str_is_email_address(s):
    if isinstance(s, str):
        return re.search('^(?P<id>.+)@(?P<domain>[\w\d]+\.([\w\d]+\.){0,}\w+$)', s)


def str2list(s):
    return [x.strip() for x in s.split(',') if x.strip()] if isinstance(s, str) else s


def arg2list(obj):
    if obj is None:
        return obj
    elif not isinstance(obj, list):
        return [obj]
    return obj


def bytes_decode(v, enconding='utf-8', errors='strict', **kwargs):
    '''
    convert v to spec type, default str, puresnmp use it.
    :param v:
    :param to_type:
    :param enconding:
    :param errors:
    :return:
    '''
    if isinstance(v, bytes):
        try:
            v = bytes.decode(v, encoding=enconding, errors=errors)
        except Exception as e:
            # if v is hex bytes
            v = v.hex()
    return change_type(v, **kwargs)


def change_type(v, to_type=None, default=None, strip=True):
    '''
    转换类型，如果有指定，但转换不了，返回default或原值，如果无指定，刚自动匹配
    :param v:
    :param _type:
    :param default: 默认返回，None则返回原值
    :param strip:
    :return:
    '''
    if to_type:
        try:
            if to_type in [str, 'str']:
                return str(v).strip() if strip else str(v)
            elif to_type in [int, 'int']:
                return int(v)
            elif to_type in [float, 'float']:
                return float(v)
        except Exception as e:
            return default if default is not None else v
    else:
        if str_is_number(v, int):
            return int(v)
        elif str_is_number(v, float):
            return float(v)
        return v


def replace(s, pats=None, default='', ret_with_pat=False, _any=False, flags=0, escape=False):
    '''
    :param s:
    :param pats:    替换特征, [(old, new)], 如果
    :param default:  如果传入的pats列表是str, 则用default的值进行替换
    :param ret_with_pat:  是否返回匹配列表
    :param _any:  匹配任意结束
    :param flags:  re flags
    :param escape:  传入的pats需要强制escape
    :return:
    '''
    if not pats:
        pats = [(r'[\r\n]+', '\n')]
    if isinstance(pats[0], str):
        pats = [(x, default) for x in pats]
    if escape:
        pats = [(re.escape(x1), x2) for x1, x2 in pats]
    _pats = '' if _any else []
    s1 = s
    for pat, rep in pats:
        s = re.sub(pat, rep, s, flags=flags)
        # 如果_any==True, 返回的_pats为str, 否则是list
        if s != s1:
            pat = pat.replace('\\', '')
            s1 = s
            if _any:
                _pats = pat
                break
            else:
                _pats.append(pat)
    if ret_with_pat:
        return s, _pats
    else:
        return s


def windows_filename(s, full=False, space=True):
    '''
    windows命名
    :param s:
    :param full: 用全角代替, 否则用_代替
    :param space: 是否替换空格
    :return:
    '''
    pats = [(r'\\', '＼'), (r'/', '／'), (r':', '：'), (r'\*', '＊'), (r'\?', '？'), (r'"', '＂'), (r'<', '＜'),
            (r'>', '＞'), (r'\|', '｜')]
    if space:
        pats.append((' ', '_'))
    if not full:
        pats = [(x[0], '_') for x in pats]
    return replace(s, pats=pats)
