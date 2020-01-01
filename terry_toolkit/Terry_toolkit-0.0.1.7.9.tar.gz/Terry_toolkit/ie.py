# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:author: seanlee97
:description: 结合LTP平台实现简单三元组抽取
:ctime: 2018.07.23 16:14
:mtime: 2018.07.23 16:14
"""
import gc
import os 
import re
import logging
import sys
if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf8")

from pyltp import Segmentor, Postagger, Parser, NamedEntityRecognizer,SementicRoleLabeller
from tqdm import tqdm
# import utils as U

from . import *
class TripleIE(object):
    def __init__(self, in_file_path='i.txt', out_file_path='o.txt', model_path='./ltp', clean_output=True):
        self.logger = logging.getLogger("TripleIE")

        self.in_file_path = in_file_path
        self.out_file_path = out_file_path
        self.model_path = model_path
        self.clean_output = clean_output  # 输出是否有提示

        self.out_handle = None

        self.segmentor = Segmentor()
        self.segmentor.load(os.path.join(self.model_path, "cws.model"))
        self.postagger = Postagger()
        self.postagger.load(os.path.join(self.model_path, "pos.model"))
        self.parser = Parser()
        self.parser.load(os.path.join(self.model_path, "parser.model"))
        self.recognizer = NamedEntityRecognizer()
        self.recognizer.load(os.path.join(self.model_path, "ner.model"))

        # self.labeller = SementicRoleLabeller()
        # self.labeller.load(os.path.join(self.model_path, 'pisrl.model'))
    def __del__(self):
        self.segmentor.release()
        # self.labeller.release()
        self.postagger.release()
        self.recognizer.release()
    def format_labelrole(self, words, postags):
        arcs = self.parser.parse(words, postags)
        roles = self.labeller.label(words, postags, arcs)
        roles_dict = {}
        for role in roles:
            roles_dict[role.index] = {arg.name:[arg.name,arg.range.start, arg.range.end] for arg in role.arguments}
        # print((words, postags, arcs))
        # print("roles_dict",roles_dict)
        del roles
        del  arcs
        del words
        del postags
        
        # print(locals().keys())
        gc.collect()
        return roles_dict
    def rm_signs(self,raw):
        return re.sub(r"[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", raw)

    def rm_html(self,raw):
        dr = re.compile(r'<[^>]+>',re.S)
        return dr.sub('',raw)

    def split_by_sign(self,raw, regex=r'[\s+\!！。？\n\t]'):
        arr = re.split(regex, raw)
        return list(filter(lambda x: len(x.strip()) > 0, arr))
    def get(self, text):
        """
        不保存文件版本
        """
 

        text = self.rm_html(text)
        # sentences = self.split_by_sign(text, regex=r'[\s+\!！。？\n\t]'):
        
        sentences = Text().sentence_segmentation_v1(text) #提取单个句子 分句

        self.logger.info("detect {} sentences".format(len(sentences)))

        self.logger.info("start to extract...")
        for sentence in sentences:
            yield self.get_extract(sentence)
    def get_test(self, sentence):
            """
            重构不保存,返回三元组数据
            """
            print('原句:',sentence)
            words = self.segmentor.segment(sentence)
            postags = self.postagger.postag(words)
            ner = self.recognizer.recognize(words, postags)
            arcs = self.parser.parse(words, postags)
            # # roles_dict=self.format_labelrole(words, postags)
            # # print("roles_dict",roles_dict)
            # # print(ner)
            for i,n in enumerate(ner):
                # print(n)
                if n =="O":
                    pass 
                else:
                    print(words[i])
                    print(n)
                    pass
 

    def get_extract(self, sentence):
        """
        重构不保存,返回三元组数据
        """
        print('原句:',sentence)
        words = self.segmentor.segment(sentence)
        postags = self.postagger.postag(words)
        # print("postags",postags)


        ner = self.recognizer.recognize(words, postags)
        # print("ner",ner)
        # for n in ner:
        #     print(n)
        arcs = self.parser.parse(words, postags)
        # # roles_dict=self.format_labelrole(words, postags)
        # # print("roles_dict",roles_dict)
        # # print(ner)
        # for i,n in enumerate(ner):
        #     # print(n)
        #     if n =="O":
        #         pass 
        #     else:
        #         print(words[i])
        #         pass
        for w,p,n,a in zip(words,postags,ner,arcs):
            print(w,p,n,a)
        sub_dicts = self._build_sub_dicts(words, postags, arcs)
        # print('sub_dicts',sub_dicts)
        for idx in range(len(postags)):
            # print(postags[idx] )
            # print(ner[idx] )

            if postags[idx] == 'v':
                # print(words[idx] )
                # print(postags)
                sub_dict = sub_dicts[idx]
                # 主谓宾
                if 'SBV' in sub_dict and 'VOB' in sub_dict:
                    e1 = self._fill_ent(words, postags, sub_dicts, sub_dict['SBV'][0])
                    r = words[idx]
                    e2 = self._fill_ent(words, postags, sub_dicts, sub_dict['VOB'][0])
                    if self.clean_output:
                        # self.out_handle.write("%s, %s, %s\n" % (e1, r, e2))
                        return e1, r, e2,'1主谓宾'
                    else:
                        # self.out_handle.write("主谓宾\t(%s, %s, %s)\n" % (e1, r, e2))
                        return e1, r, e2,'主谓宾'
                    # self.out_handle.flush()
                # 定语后置，动宾关系
                if arcs[idx].relation == 'ATT':
                    if 'VOB' in sub_dict:
                        e1 = self._fill_ent(words, postags, sub_dicts, arcs[idx].head - 1)
                        r = words[idx]
                        e2 = self._fill_ent(words, postags, sub_dicts, sub_dict['VOB'][0])
                        temp_string = r+e2
                        if temp_string == e1[:len(temp_string)]:
                            e1 = e1[len(temp_string):]
                        if temp_string not in e1:
                            if self.clean_output:
                                # self.out_handle.write("%s, %s, %s\n" % (e1, r, e2))
                                return e1, r, e2,'1动宾定语后置'
                            else:
                                # self.out_handle.write("动宾定语后置\t(%s, %s, %s)\n" % (e1, r, e2))
                                 return e1, r, e2,'动宾定语后置'
                            
                            # self.out_handle.flush()

            # 抽取命名实体有关的三元组
            try:
                if ner[idx][0] == 'S' or ner[idx][0] == 'B':
                    ni = idx
                    if ner[ni][0] == 'B':
                        while len(ner) > 0 and len(ner[ni]) > 0 and ner[ni][0] != 'E':
                            ni += 1
                        e1 = ''.join(words[idx:ni+1])
                    else:
                        e1 = words[ni]
                    if arcs[ni].relation == 'ATT' and postags[arcs[ni].head-1] == 'n' and ner[arcs[ni].head-1] == 'O':
                        r = self._fill_ent(words, postags, sub_dicts, arcs[ni].head-1)
                        if e1 in r:
                            r = r[(r.idx(e1)+len(e1)):]
                        if arcs[arcs[ni].head-1].relation == 'ATT' and ner[arcs[arcs[ni].head-1].head-1] != 'O':
                            e2 = self._fill_ent(words, postags, sub_dicts, arcs[arcs[ni].head-1].head-1)
                            mi = arcs[arcs[ni].head-1].head-1
                            li = mi
                            if ner[mi][0] == 'B':
                                while ner[mi][0] != 'E':
                                    mi += 1
                                e = ''.join(words[li+1:mi+1])
                                e2 += e
                            if r in e2:
                                e2 = e2[(e2.idx(r)+len(r)):]
                            if r+e2 in sentence:
                                if self.clean_output:
                                    # self.out_handle.write("%s, %s, %s\n" % (e1, r, e2))
                                    return e1, r, e2,"1人名/地名/机构"
                                else:
                                    # self.out_handle.write("人名/地名/机构\t(%s, %s, %s)\n" % (e1, r, e2))
                                    return e1, r, e2,"人名/地名/机构"
                                
                                # self.out_handle.flush()
            except:
                return
                pass

    
    def run(self, in_file_path=None, out_file_path=None):
        if in_file_path is not None:
            self.in_file_path = in_file_path
        if out_file_path is not None:
            self.out_file_path = out_file_path

        self.out_handle = open(self.out_file_path, 'a')

        with open(self.in_file_path, "r", encoding="utf-8") as rf:
            self.logger.info("loadding input file {}...".format(self.in_file_path))
            text = ""
            for line in rf:
                line = line.strip()
                text += line
            self.logger.info("done with loadding file...")

            text = self.rm_html(text)
            sentences = self.split_by_sign(text)

            self.logger.info("detect {} sentences".format(len(sentences)))

            self.logger.info("start to extract...")
            for sentence in tqdm(sentences):
                self.extract(sentence)

            self.logger.info("done with extracting...")
            self.logger.info("output to {}".format(self.out_file_path))
            
        # close handle
        self.out_handle.close()

    def extract(self, sentence):
        words = self.segmentor.segment(sentence)
        postags = self.postagger.postag(words)
        ner = self.recognizer.recognize(words, postags)
        arcs = self.parser.parse(words, postags)

        sub_dicts = self._build_sub_dicts(words, postags, arcs)
        for idx in range(len(postags)):

            if postags[idx] == 'v':
                sub_dict = sub_dicts[idx]
                # 主谓宾
                if 'SBV' in sub_dict and 'VOB' in sub_dict:
                    e1 = self._fill_ent(words, postags, sub_dicts, sub_dict['SBV'][0])
                    r = words[idx]
                    e2 = self._fill_ent(words, postags, sub_dicts, sub_dict['VOB'][0])
                    if self.clean_output:
                        self.out_handle.write("%s, %s, %s\n" % (e1, r, e2))
                    else:
                        self.out_handle.write("主谓宾\t(%s, %s, %s)\n" % (e1, r, e2))
                    self.out_handle.flush()
                # 定语后置，动宾关系
                if arcs[idx].relation == 'ATT':
                    if 'VOB' in sub_dict:
                        e1 = self._fill_ent(words, postags, sub_dicts, arcs[idx].head - 1)
                        r = words[idx]
                        e2 = self._fill_ent(words, postags, sub_dicts, sub_dict['VOB'][0])
                        temp_string = r+e2
                        if temp_string == e1[:len(temp_string)]:
                            e1 = e1[len(temp_string):]
                        if temp_string not in e1:
                            if self.clean_output:
                                self.out_handle.write("%s, %s, %s\n" % (e1, r, e2))
                            else:
                                self.out_handle.write("动宾定语后置\t(%s, %s, %s)\n" % (e1, r, e2))
                            
                            self.out_handle.flush()

            # 抽取命名实体有关的三元组
            try:
                if ner[idx][0] == 'S' or ner[idx][0] == 'B':
                    ni = idx
                    if ner[ni][0] == 'B':
                        while len(ner) > 0 and len(ner[ni]) > 0 and ner[ni][0] != 'E':
                            ni += 1
                        e1 = ''.join(words[idx:ni+1])
                    else:
                        e1 = words[ni]
                    if arcs[ni].relation == 'ATT' and postags[arcs[ni].head-1] == 'n' and ner[arcs[ni].head-1] == 'O':
                        r = self._fill_ent(words, postags, sub_dicts, arcs[ni].head-1)
                        if e1 in r:
                            r = r[(r.idx(e1)+len(e1)):]
                        if arcs[arcs[ni].head-1].relation == 'ATT' and ner[arcs[arcs[ni].head-1].head-1] != 'O':
                            e2 = self._fill_ent(words, postags, sub_dicts, arcs[arcs[ni].head-1].head-1)
                            mi = arcs[arcs[ni].head-1].head-1
                            li = mi
                            if ner[mi][0] == 'B':
                                while ner[mi][0] != 'E':
                                    mi += 1
                                e = ''.join(words[li+1:mi+1])
                                e2 += e
                            if r in e2:
                                e2 = e2[(e2.idx(r)+len(r)):]
                            if r+e2 in sentence:
                                if self.clean_output:
                                    self.out_handle.write("%s, %s, %s\n" % (e1, r, e2))
                                else:
                                    self.out_handle.write("人名/地名/机构\t(%s, %s, %s)\n" % (e1, r, e2))
                                
                                self.out_handle.flush()
            except:
                pass

    """
    :decription: 为句子中的每个词语维护一个保存句法依存儿子节点的字典
    :args:
        words: 分词列表
        postags: 词性列表
        arcs: 句法依存列表
    """
    def _build_sub_dicts(self, words, postags, arcs):
        sub_dicts = []
        for idx in range(len(words)):
            sub_dict = dict()
            for arc_idx in range(len(arcs)):
                if arcs[arc_idx].head == idx + 1:
                    if arcs[arc_idx].relation in sub_dict:
                        sub_dict[arcs[arc_idx].relation].append(arc_idx)
                    else:
                        sub_dict[arcs[arc_idx].relation] = []
                        sub_dict[arcs[arc_idx].relation].append(arc_idx)
            sub_dicts.append(sub_dict)
        return sub_dicts

    """
    :decription:完善识别的部分实体
    """
    def _fill_ent(self, words, postags, sub_dicts, word_idx):
        sub_dict = sub_dicts[word_idx]
        prefix = ''
        if 'ATT' in sub_dict:
            for i in range(len(sub_dict['ATT'])):
                prefix += self._fill_ent(words, postags, sub_dicts, sub_dict['ATT'][i])
        
        postfix = ''
        if postags[word_idx] == 'v':
            if 'VOB' in sub_dict:
                postfix += self._fill_ent(words, postags, sub_dicts, sub_dict['VOB'][0])
            if 'SBV' in sub_dict:
                prefix = self._fill_ent(words, postags, sub_dicts, sub_dict['SBV'][0]) + prefix

        return prefix + words[word_idx] + postfix
