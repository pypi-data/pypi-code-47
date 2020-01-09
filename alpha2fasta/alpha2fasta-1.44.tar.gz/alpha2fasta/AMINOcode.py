import re
import unidecode #pip
import numpy as np

global aminoCode_table
aminoCode_table = {
      "a": "YA",
      "b": "E",
      "c": "C",
      "d": "D",
      "e": "YE",
      "f": "F",
      "g": "G",
      "h": "H",
      "i": "YI",
      "j": "I",
      "k": "K",
      "l": "L",
      "m": "M",
      "n": "N",
      "o": "YQ",
      "p": "P",
      "q": "Q",
      "r": "R",
      "s": "S",
      "t": "T",
      "u": "YV",
      "v": "V",
      "x": "W",
      "z": "A",
      "w": "YW",
      "y": "YY",
      ".": "YP",
      "9": "YD",
      " ": "YS"
}
global aminoCode_table_2
aminoCode_table_2 = {
      "0": "YDA",
      "1": "YDQ",
      "2": "YDT",
      "3": "YDH",
      "4": "YDF",
      "5": "YDI",
      "6": "YDS",
      "7": "YDE",
      "8": "YDE",
      "9": "YDN",
      ".": "YPE",
      ",": "YPC",
      ";": "YPS",
      "!": "YPW",
      "?": "YPQ",
      ":": "YPT",
}
def AMINOcode(text,simplified=False):
    global aminoCode_table
    try:
        text = text.decode('utf-8') #decode
    except:
        pass
    text = unidecode.unidecode(text) #remove accents
    text = text.lower() #lower case
    text = re.sub('\s',' ',text) #sub all spaces to " "
    if not simplified:
        global aminoCode_table_2
        for k,v in aminoCode_table_2.items():
            text = text.replace(k, v)
    else:
        text = re.sub('[,;!?:]','.',text) #sub all punctuation to "."
        text = re.sub('\d','9',text) #sub all numbers to 9
    for k,v in aminoCode_table.items():
        text = text.replace(k, v)
    for c,i in enumerate(text.lower()):
        if i not in aminoCode_table:
            text=re.sub('\\'+i,'YK',text)
    return (text)
    
def AMINOcode_reverse(text,simplified=False):
    global aminoCode_table
    if not simplified:
        global aminoCode_table_2
        for key,value in aminoCode_table_2.items(): #iteritems
            if re.search('Y[DP]\w',value):
                text = re.sub(value,key,text)
    for key,value in aminoCode_table.items():
        if re.search('Y\w',value):
            text = re.sub(value,key,text)
    text = re.sub('YK','-',text)
    text=np.array(re.findall('.',text))
    for key,value in aminoCode_table.items():
        text[text==value]=key
    text=''.join(text)
    return text