# -*- coding: gbk -*-
import json
import numpy as np
import jieba
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
import re
#输入段落预处理
def input_preproccess(p):
    input_sentences=[]
    sentences = re.split('[。？！]',p)
    for sentence in sentences:
        if sentence!='':
            sentence = re.sub('[\u3002\uff1f\uff01\uff0c\u3001|\uff1b\uff1a\u201c\u201d\u2018\u2019\uff08\uff09\u300a\u300b\u3008\u3009\u3010\u3011\u300e\u300f\u300c\u300d\ufe43\ufe44\u3014\u3015\u2026\u2014\uff5e\ufe4f\uffe5]',"", sentence)
            input_chinese = "".join(re.findall("[\u4e00-\u9fa5\d]+", sentence))
            if len(input_chinese) > 4:
                input_sentences.append(input_chinese)
    return input_sentences

#生成输入段落句向量
def get_input_vector(p):
    import synonyms
    input_sentence_vectors=[]
    input_sentences=input_preproccess(p)
    for sentence in input_sentences:
        input_vectors = []
        input_vector = np.zeros((100,))
        cut_p = jieba.lcut(sentence)
        for cut in cut_p:
            try:
                p_vector = synonyms.v(cut)
                input_vector += p_vector
            except:
                pass
        input_vectors.append(input_vector)
        input_vectors = np.array(input_vectors)
        input_sentence_vectors.append(input_vectors)
    return input_sentence_vectors
#预测结果
def predict_result(p):
    knowledges_collection={}
    hottopics_collection={}
    knowledge_total = []
    for paragraph_text in p:
        hottopic_total=[]
        input_sentence_vectors=get_input_vector(paragraph_text)
        for sentence_vectors in input_sentence_vectors:
            section_model=joblib.load('paragraph data/lr_section.pkl')
            probability=section_model.predict_proba(sentence_vectors)
            hottopic_probability=float(probability[0][0])
            knowledge_probability=float(probability[0][1])
            hottopic_total.append(hottopic_probability)
            knowledge_total.append(knowledge_probability)
        try:
            hottopic_result=sum(hottopic_total)/len(hottopic_total)
            knowledge_result=sum(knowledge_total)/len(knowledge_total)
            if knowledge_result > hottopic_result:
                knowledges_collection[paragraph_text] = knowledge_result
            else:
                hottopics_collection[paragraph_text] = hottopic_result
        except:
            pass
    knowledges_collection_sort=sorted(knowledges_collection.items(),key=lambda x:x[1],reverse=True)
    hottopics_collection_sort=sorted(hottopics_collection.items(),key=lambda x:x[1],reverse=True)
    return  knowledges_collection_sort,hottopics_collection_sort
#提取知识结果
def get_knowledge_result(p):
    knowledges_collection_sort, hottopics_collection_sort=predict_result(p)
    knowledges={}
    get_knowledges=[]
    for i in knowledges_collection_sort:
        if i[1]>=0.7:
            get_knowledges.append(i[0])
    knowledges['text_type']='知识文章'
    knowledges['get_knowledge']=get_knowledges
    return knowledges
#提取热点结果
def get_hottopic_result(p):
    knowledges_collection_sort, hottopics_collection_sort = predict_result(p)
    hottopics = {}
    get_hottopics=[]
    for i in hottopics_collection_sort:
        if i[1]>=0.7:
            get_hottopics.append(i[0])
    hottopics['text_type'] = '热点文章'
    hottopics['get_hottopic'] = get_hottopics
    print(hottopics)
    return hottopics
#提取混合结果
def get_complete_result(p):
    knowledges_collection_sort, hottopics_collection_sort = predict_result(p)
    complex= {}
    collect = []
    get_knowledges_two=[]
    get_hottopics_two=[]
    no_marks_knowledge=[]
    no_marks_hottopics=[]
    for i in hottopics_collection_sort:
        dict_hottopic = {}
        dict_hottopic['段落'] = i[0]
        if i[1] >= 0.7:
            dict_hottopic['热点率'] = i[1]
            get_hottopics_two.append(i[0])
        else:
            dict_hottopic['无标记'] = i[1]
            no_marks_hottopics.append(i[0])
        if len(dict_hottopic) == 2:
            collect.append(dict_hottopic)
    for j in knowledges_collection_sort:
        dict_knowledge = {}
        dict_knowledge['段落'] = j[0]
        if j[1] >= 0.7:
            dict_knowledge['知识率'] = j[1]
            get_knowledges_two.append(j[0])
        else:
            dict_knowledge['无标记'] = j[1]
            no_marks_knowledge.append(j[0])
        if len(dict_knowledge) == 2:
            collect.append(dict_knowledge)
    hs=[]
    ks=[]
    for d in collect:
        for k in d.keys():
            if k=='热点率':
                hs.append(k)
            if k=="知识率":
                ks.append(k)
    if len(hs)/len(collect)>=0.7:
        complex['text_type'] = '热点文章'
        complex['get_hottopic'] = get_hottopics_two
    if len(ks)/len(collect)>=0.7:
        complex['text_type']='知识文章'
        complex['get_knowledge']=get_knowledges_two
    else:
        complex['text_type'] = '综合文章'
        if get_hottopics_two==[]:
            complex['get_hottopic'] = no_marks_hottopics
        else:
            complex['get_hottopic'] = get_hottopics_two
        if get_knowledges_two==[]:
            complex['get_knowledge']=no_marks_knowledge
        else:
            complex['get_knowledge'] = get_knowledges_two
    return complex

def get_paragraph_result(p):
    knowledges_collection_sort,hottopics_collection_sort=predict_result(p)
    if len(knowledges_collection_sort)/len(p)>=0.7:
        return get_knowledge_result(p)
    if len(hottopics_collection_sort)/len(p)>=0.7:
        return get_hottopic_result(p)
    if len(knowledges_collection_sort)!=0 and len(hottopics_collection_sort)!=0:
        if len(knowledges_collection_sort) / len(p) < 0.7 and len(hottopics_collection_sort) / len(p) < 0.7:
            return get_complete_result(p)
