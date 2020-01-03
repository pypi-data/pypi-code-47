import xml.etree.ElementTree as ET
import re
def not_empty(s): return s and s.strip()   
def rm_alpha(lst): 
    [lst.remove(i) for i in lst if type(i) == type(1450)]
    return lst
def keywd(wd_dict,num):
    lst=list()
    for rk in range(num):
        lst.extend( rm_alpha( list(wd_dict[rk])))	
    return lst
def kwd_search(lst,num):   
    wd_dict, kwd_lst, comm_wd=dict(), list(), list()
    with open ( 'filter.txt', 'r', encoding = 'utf8') as file:   
	    [comm_wd.append( word.rstrip('\n')) for word in file]
	[wd_dict.setdefault(i,lst.count(i)) for i in set(lst) if i not in wd_dict.keys()]           
	[wd_dict.pop(x, None) for x in comm_wd]       
	wd_dict=sorted(wd_dict.items(), key=lambda wd_dict:wd_dict[1] ,reverse=True)  
	kwd_lst=keywd(wd_dict,num)
    lst.clear()
    return kwd_lst
def xmlExtKwd(XML,txt,num):     
    wd_lst=list()
    text_lst, tail_lst=['p','claim-text','heading'], ['claim-ref','figref','b']
    with open( XML, 'r', encoding = 'utf8') as f0, open( txt, 'w+', encoding = 'utf8') as f1:
        for event,elem in ET.iterparse(f0):
            if  event == 'end':
                if ( elem.tag in text_lst ) and ( elem.text != None ): f1.write(elem.text+'\n')                 
                if ( elem.tag in tail_lst ) and ( elem.tail != None ): f1.write(elem.tail)                   
            elem.clear()
        f1.seek(0)
        for li in f1.readlines():       
            li_lst=re.sub("[,.;'\n]"," ",li.lower()).split(' ')
            wd_lst.extend(filter(not_empty, li_lst))  
    return kwd_search(wd_lst,num)