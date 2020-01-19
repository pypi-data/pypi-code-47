#!/usr/bin/env python
# encoding: utf-8

import sys


PYTHON_VERSION = sys.version_info.major
PYTHON_VERSION_LESS_THAN_3 = PYTHON_VERSION < 3


# patterns
_heb = r"[א-ת]" + "{1,}[\']?[\"]*" + "[א-ת]" + "{1,}|" + "[א-ת]"
_eng = r"[a-zA-Z]{1,}[\']?[\"]*[a-zA-Z0-9]{1,}|[a-zA-Z][a-zA-Z0-9]*"
_eng_abbrev = r"[a-zA-Z]{1}\.[a-zA-Z]{1}(\.[a-zA-Z]){0,1}"
_hour = r"[0-2]?[0-9]:[0-5][0-9]"
_date1 = r"[0-9]{1,3}-[0-9]{1,3}-([1-2][0-9])?[0-9][0-9]"
_date2 = r"([0-9]{1,3}-)?[0-9]{1,3}[\./][0-9]{1,3}[\./]([1-2][0-9])?[0-9][0-9]"
_num = r"[+-]?([0-9]+[0-9/-]*[\.]?[0-9]+|[0-9]+)%{0,1}"
_url = r"[a-z]+://\S+"
_email = r".+@.+\..+"
_punc = r"[,;:\-&!\?\.\]/)'`\"\*\+=_~}\[('`\"{/\\\<\>#%]" #—–]"
_bad_punc = r"[\'\"]"
_bom = r"\xef\xbb\xbf|\ufeff|\u200e"
_other = r"\xa0|\xe2?\x80\xa2?[[^׳-׳×a-zA-Z0-9!\?\.,:;\-()\[\]{}]+"
_whitespace = r"\s+"
_linebreaks = r"{3,}|".join(['\\' + x for x in ['*', '_', '.', '\\', '!', '+', '>', '<', '#', '^', '~', '=', '-']]) + '\n'
_repeated = r"\S*(\S)\1{3,}\S*"


# group names
class Groups(object):
    WHITESPACE = 'WS'
    DATE = 'DATE'
    HOUR = 'HOUR'
    NUMBER = 'NUM'
    URL = 'URL'
    PUNCTUATION = 'PUNC'
    ENGLISH = 'ENG'
    HEBREW = 'HEB'
    OTHER = 'OTHER'


# pattern 2 group mapping
patterns = [
    (_whitespace, Groups.WHITESPACE),
    (_linebreaks, None),
    (_repeated, None),
    (_bom, None),
    (_date1, Groups.DATE),
    (_date2, Groups.DATE),
    (_hour, Groups.HOUR),
    (_num, Groups.NUMBER),
    (_url, Groups.URL),
    (_eng_abbrev, Groups.ENGLISH),
    (_punc, Groups.PUNCTUATION),
    (_eng, Groups.ENGLISH)]

if PYTHON_VERSION_LESS_THAN_3:
    patterns += [(_heb.decode('utf-8'), Groups.HEBREW)]

patterns += [
    (_heb, Groups.HEBREW),
    (_other, Groups.OTHER)]



def tokenize(text, with_whitespaces=False):
    # input: text
    # outputs: generator -> yields tuple(GROUP, TOKEN, TOKEN_NUM, (START_IDX, END_IDX))

    yield None



if __name__ == '__main__':
    sent = 'aspirin   aaaaaa  aaaaaaaaaaa —–  dipyridamole'
    sent_tokens = tokenize(sent)
    for st in sent_tokens:
        print(st)

