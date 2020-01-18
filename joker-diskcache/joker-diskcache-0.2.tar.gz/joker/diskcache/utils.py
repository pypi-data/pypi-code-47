#!/usr/bin/env python3
# coding: utf-8
import hashlib
import re
import os
import zlib

windows_reserved_names = {
    'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4',
    'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2',
    'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9',
}


def windows_filename_safe(s, repl='_'):
    # <>:"/\\|?* and ASCII 0 - 31
    # https://stackoverflow.com/a/31976060/2925169
    ordinals = [ord(c) for c in '<>:"/\\|?*']
    ordinals.extend(range(32))
    s = s.translate(dict.fromkeys(ordinals, repl))
    if s.endswith('.'):
        s = s[:-1]
    if s.upper() in windows_reserved_names:
        s += '_'
    return s


def proper_filename(s):
    s = windows_filename_safe(s.strip(), '_')
    # replace leading .-, quotes/spaces with _
    s = re.sub(r'^-', '_', s)
    s = re.sub(r"['\s]+", '_', s)
    s = re.sub(r'\s*\(([0-9]+)\)\.', r'-\1.', s)
    return s


def standard_path(dirpath, key, prefixlen=4):
    prefix = key[:prefixlen]
    pdirpath = os.path.join(dirpath, prefix)
    if not os.path.isdir(pdirpath):
        os.makedirs(pdirpath, exist_ok=True)
    return os.path.join(pdirpath, key)


def proper_path(dirpath, name, prefixlen=4):
    name = proper_filename(name)
    chksum = hashlib.md5(name.encode('utf-8')).hexdigest()
    key = chksum + '.' + name
    return standard_path(dirpath, key, prefixlen)


def compress(content, compression):
    # currently gzip only
    if compression == 'auto' and need_for_compression(content):
        compression = 'gzip'
    if compression == 'gzip':
        return zlib.compress(content), compression
    return content, None


def decompress(content, compression):
    if compression == 'gzip':
        return zlib.decompress(content)
    return content


def need_for_compression(content):
    thr = 503
    n = len(content)
    if n < thr:
        return False
    step = int(n / thr)
    if step == 1:
        samp = content[-thr:]
    else:
        samp = content[::step]
    return len(set(samp)) < 90
