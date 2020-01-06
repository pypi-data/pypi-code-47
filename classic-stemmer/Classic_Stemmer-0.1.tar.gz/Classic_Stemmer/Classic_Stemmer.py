# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:18:44 2020

@author: Abhilash
Reimplementation of the
`Porter stemming algorithm <http://tartarus.org/~martin/PorterStemmer/>`_
in Python.
"""
import re

list_step_2={
        "ational":"ate",
        "tional":"tion",
        "enci":"ence",
        "anci":"ance",
        "izer":"ize",
        "abli":"able",
        "alli":"al",
        "entli":"ent",
        "eli":"e",
        "ousli":"ous",
        "ization":"ize",
        "ation":"ate",
        "ator":"ate",
        "alism":"al",
        "iveness":"ive",
        "fulness":"ful",
        "ousness":"ous",
        "aliti":"al",
        "iviti":"ive",
        "biliti":"ble"
        }


list_step_3={
          "icate":"ic",
          "ative":"",
          "alize":"al",
          "iciti":"ic",
          "ical":"ic",
          "ful":"",
          "ness":""}

vowels="[aeiouy]"
consonants="[^aeiou]"
vowels_sequence="[aeiouy]+"
consonants_sequence="[^aeiou]+"

mgr0=re.compile("^("+consonants_sequence+")?" + vowels_sequence +  consonants_sequence)
meq0=re.compile("^("+consonants_sequence+")?" + vowels_sequence + consonants_sequence + "("+consonants_sequence+")?$")
mgr1=re.compile("^("+consonants_sequence+")?" + vowels_sequence+consonants_sequence+vowels_sequence + consonants_sequence)
vowel_in_stem=re.compile("^("+consonants_sequence+")?" + vowels)
ends_with_cvc= re.compile("^" + consonants_sequence+vowels_sequence+consonants_sequence)

ed_ing_form=re.compile("^(.*)(ed|ing)$")
at_bl_iz_form=re.compile("(at|bl|iz)$")
step1b= re.compile("([^aeiouylsz])\\$")
step2=re.compile("^(.+?)(ational|tional|enci|anci|izer|bli|alli|entli|eli|ousli|ization|ation|ator|alism|iveness|fulness|ousness|aliti|iviti|biliti|logi)$")
step3=re.compile("^(.+?)(icate|ative|alize|iciti|ical|ful|ness)$")
step4_1=re.compile("^(.+?)(al|ance|ence|er|ic|able|ible|ant|ement|ment|ent|ou|ism|ate|iti|ous|ive|ize)$")
step4_2=re.compile("^(.+?)(s|t)(ion)$")
step5=re.compile("^(.+?)e$")

def stem(v):
    if(len(v)<3):
        return v
    if(v[0]=="y"):
        v="Y"+v[1:]
        
    #step1
    if v.endswith("s"):
        if v.endswith("sses"):
            v=v[:-2]
        elif v.endswith("ies"):
            v=v[:-2]
        elif v[-2]!="s":
            v=v[:-1]
            
    #step1b
    if v.endswith("eed"):
        s=v[:-3]
        #if m>0
        if mgr0(s):
            v=v[:-1]
            #else ed_ing
        else:
            m=ed_ing_form.match(v)
            if m:
                st=m.group(1)
                #check for vowel in stem *v*
                if vowel_in_stem.match(st):
                    v=st
                    #if at|bl|iz
                    if at_bl_iz_form.match(v):
                        
                        v+="e"
                        #elif *d and(*l or* s* z)
                    elif step1b.match(st):
                        
                        v=v[:-1]
                    elif ends_with_cvc.match(st):
                        v+="e"
    
                        
    #step1c-> y|i
    if v.endswith("y"):
        st=v[:-1]
        if vowel_in_stem.match(st):
            v=st+"i"
    
    #step2
    m_2=step2.match(v)
    if m_2:
        st=m_2.group(1)
        suff=m_2.group(2)
        if mgr0.match(st):
            v=st+list_step_2[suff]
    
    #step3
    m_3=step3.match(v)
    if m_3:
        st=m_3.group(1)
        suff=m_3.group(2)
        if mgr0.match(st):
            v=st+list_step_3[suff]
    
    #step4a
    m_4=step4_1.match(v)
    if m_4:
        st=m_4.group(1)
        if mgr1.match(st):
            v=st
    #step4b
    else:
        m_5=step4_2.match(v)
        if m_5:
            st=m_5.group(1)
            if mgr1.match(st):
                v=st
    #step 5a
    m_5=step5.match(v)
    if m_5:
        st=m_5.group(1)
        if mgr1.match(st):
            v=st
        elif mgr0.match(st) and not ends_with_cvc.match(st):
            v=st
    if v.endswith("ll") and mgr1.match(v):
        v=v[:-1]
    if v[0]=='y':
        v='y'+v[1:]
        
    
    return v

if __name__=="__main__":
    print(stem("probate"))
    print(stem("fundamentally"))
        
        
        
    
    
        
        
            
        









