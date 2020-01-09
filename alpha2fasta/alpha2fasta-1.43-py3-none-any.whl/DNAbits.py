import re
import numpy as np

def to_bin(string):
    res = ''
    for char in string:
        tmp = bin(ord(char))[2:]
        tmp = '%08d' %int(tmp)
        tmp=tmp[::-1] #???
        res += tmp
    return res
def to_str(string):
    res = ''
    for idx in range(len(string)/8):
        cstr = string[idx*8:(idx+1)*8]
        cstr=cstr[::-1] #???
        tmp = chr(int(cstr, 2))
        res += tmp
    return res


def DNAbits(text):
    text=to_bin(text)
    text_0 = re.findall('.',text[0:len(text)-1:2])
    text_1 = re.findall('.',text[1:len(text):2])
    text = np.transpose(np.array([(text_0),(text_1)]))
    text = text.astype(int)
    text = text * [1,2]
    text = np.sum(text,1)
    text = text.astype(str)
    text[text=='0']='A'
    text[text=='1']='C'
    text[text=='2']='G'
    text[text=='3']='T'
    text=''.join(text)
    return text
    
def DNAbits_reverse(dna):
    text = np.zeros((len(dna),2)).astype(int)
    dna=np.array(re.findall('.',dna))
    text[dna=='A']=[0,0]
    text[dna=='C']=[1,0]
    text[dna=='G']=[0,1]
    text[dna=='T']=[1,1]
    text=text.astype(str)
    text=''.join(np.concatenate(text))
    text=to_str(text)
    return text