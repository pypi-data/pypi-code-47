#!/usr/bin/env python3
# coding: utf-8

import gzip
import hashlib
import logging
import os
import traceback

from joker.diskcache import utils

logger = logging.getLogger(__name__)


class SimpleDiskCache(object):
    def __init__(self, dirpath, prefixlen=4):
        os.makedirs(dirpath, exist_ok=True)
        self.dirpath = dirpath
        self.prefixlen = prefixlen

    def get_path(self, key):
        return utils.proper_path(self.dirpath, key, self.prefixlen)

    def load(self, key):
        path = self.get_path(key)
        if not os.path.exists(path):
            return
        logger.debug('use cached: ' + path)
        try:
            content = gzip.open(path).read()
            hb = content[-16:]
            content = content[:-16]
            if hashlib.md5(content).digest() == hb:
                return content
            logger.debug('md5 hash mismatch')
        except IOError:
            traceback.print_exc()

    def save(self, key, content):
        path = self.get_path(key)
        logger.debug('save to cache: ' + path)
        hb = hashlib.md5(content).digest()
        with gzip.open(path, 'wb') as fout:
            fout.write(content)
            fout.write(hb)
        return content
