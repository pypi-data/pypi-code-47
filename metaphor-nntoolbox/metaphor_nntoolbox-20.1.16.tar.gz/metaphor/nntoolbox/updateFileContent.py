'''
Created on 20 nov. 2018

@author: jeanluc
'''
import sys, os
#from metaphor.nntoolbox.utils import replaceIncludePart

def get_start_end_indexes(start_mark, end_mark, filename):
    content = []
    if os.path.exists(filename):
        with open(filename, "r", encoding='ISO-8859-15') as ff:
            content = [val.strip("\n") for val in ff.readlines()]
    startindex = []
    endindex = []
    for ind, line in enumerate(content):
        if line.startswith(start_mark):
            startindex.append(ind)
        if line.startswith(end_mark):
            endindex.append(ind)
    return startindex, endindex, content
        
def replaceIncludePart(filesource, filetarget, start_mark="", end_mark="", finalfilename="auto", doprint=False):
    if doprint:
        print("replaceIncludePart start")
        print("source : {0}".format(filesource))
        print("target : {0}".format(filetarget))
    if not start_mark:
        start_mark = "#include_start"
    if not end_mark:
        end_mark = "#include_end"
    tgstartindex, tgendindex, tgcontent = get_start_end_indexes(start_mark, end_mark, filetarget)
    if not len(tgstartindex) * len(tgendindex):
        return
    startindex, endindex, content = get_start_end_indexes(start_mark, end_mark, filesource)
    cible = tgcontent[:tgstartindex[0]] + content[startindex[0]:endindex[0]] + tgcontent[tgendindex[0]:]
    if finalfilename:
        if finalfilename =='auto':
            finalfilename = filetarget
        with open(finalfilename, "w") as ff:
            for ind, line in enumerate(cible):
                if not ind:
                    ff.write("{0}".format(line))
                else:
                    ff.write("\n{0}".format(line))
    if doprint:
        print("replaceIncludePart end")
    return cible

if __name__ == '__main__':
    doprint = False
    res = []
    try:
        index = sys.argv.index('replaceIncludePart')
    except ValueError:
        index = 0
        
    if (index >= 0) and (len(sys.argv) >= index + 3):
        filesource = sys.argv[index + 1]
        filetarget = sys.argv[index + 2]
        
        res = replaceIncludePart(filesource, filetarget, finalfilename="auto", doprint=doprint)
    if doprint:
        for val in res:
            print(val)
