# encoding: utf-8

import hashlib
import asyncio
import jieba.analyse

from redis    import hit
from operator import itemgetter


class SimHash(object):


    def __init__(self, path_config=None, num_drawer=4, max_distance=3, num_words=100, retry=10):

        self.path_config  = path_config
        self.num_drawer   = num_drawer
        self.max_distance = max_distance
        self.num_words    = num_words
        # self.num_bits    = 256
        # self.num_bits     = 64
        self.num_bits     = 32
        self.retry        = retry



    def preprocess_keywords(self, doc):

        # pos = ('n' , 's' , 't'  , 'nr' , 'ns' ,
        #        'nt', 'nw', 'nz' , 'v'  , 'vd' ,
        #        'vn', 'a' , 'ad' , 'an' , 'd'  ,
        #         'm', 'q' , 'PER', 'LOC', 'ORG', 'TIME')

        pos = ('n', 'nr', 'ns', 'nt', 'nw', 'nz')
        # pos = ('nr', 'ns', 'nt', 'nw', 'nz')
        # pos = ('ns', 'n', 'vn', 'v')
        # pos = ('ns', 'nt', 'nw', 'nz')

        # kww = jieba.analyse.extract_tags(doc, topK=self.num_words, withWeight=True, allowPOS=pos)
        # kww = jieba.analyse.textrank(doc, topK=self.num_words, withWeight=True, allowPOS=pos)

        kww = jieba.analyse.textrank(doc, withWeight=True, allowPOS=pos)
        kww.sort(key=itemgetter(1), reverse=True)
        kww = kww[:self.num_words]

        try:
            keywords, weights = zip(*kww)
        except:
            keywords, weights = [], []

        return keywords, weights


    
    def preprocess_hash(self, keywords):

        # hashkeywords = [format(int(hashlib.sha256(kw.encode()).hexdigest(),16),'b')\
        # hashkeywords = [format(int(hashlib.blake2b(kw.encode(), digest_size=8).hexdigest(),16),'b')\
        hashkeywords = [format(int(hashlib.blake2b(kw.encode(), digest_size=4).hexdigest(),16),'b')\
                        .zfill(self.num_bits)
                        for kw in keywords]

        return hashkeywords



    def preprocess_num(self, num):

        return 1 if 1 == int(num) else -1



    def preprocess_fingerprint(self, hashkeywords, weights):

        length_words = len(hashkeywords)

        fingerprint = ''.join([str(int(sum([self.preprocess_num(hashkeywords[j][i])*weights[j]
                      for j in range(length_words)])>0))
                      for i in range(self.num_bits)])

        return fingerprint



    def preprocess(self, title, content):

        doc               = title + content
        keywords, weights = self.preprocess_keywords(doc)
        hashkeywords      = self.preprocess_hash(keywords)
        fingerprint       = self.preprocess_fingerprint(hashkeywords, weights)

        return fingerprint



    def fit_predict(self, title, content):

        fingerprint = self.preprocess(title, content)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # eid, ename  = asyncio.get_event_loop()\
        eid, ename  = loop.run_until_complete(hit(fingerprint,
                                              title,
                                              self.num_drawer,
                                              self.max_distance,
                                              self.path_config,
                                              self.retry))

        return eid, ename
