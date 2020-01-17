'''
Created on 10 févr. 2019

@author: jeanluc
'''
import os, sys

from argparse import ArgumentParser, FileType

from ....nntoolbox.filetoolbox import getDictFromGmx, findFile
from ....nntoolbox.utils import make_intern, DEMO_DEBUG_USAGE, isFloatEx, \
    isFloat, set2Float, getListFromStr

from .. import _api_service as nn1serv

# DEBUG_USE = 1  # Attention ici

def getCommandLineUsageOptions(args):
    caller = int(os.environ.get('CALLER', "0"))
    
    parser = ArgumentParser(description='Metaphor.', fromfile_prefix_chars='@') 

    parser.add_argument('-d', '--data', type=str, default="", dest="usagedata",
        nargs='+', help="Data to be evaluated. semicolon separated list 'id;inputs'")

    parser.add_argument('-sd', '--datarange', default="", 
        help="Range for training data (Excel-like files)")

    parser.add_argument('-sf', '--datafields', default=[], 
        help="Range for training data (Excel-like files)")

    parser.add_argument('-gl', '--grouplist', default=[], 
        help="lit of data field appli types")

    parser.add_argument('-db', '--debug', default=0, help="Debug state. Default 0")
    
    parser.add_argument('-L', '--leveragethreshold', type=float, default=0,
        help="leverage selection threshold. Default 0.0")

    parser.add_argument('-de', '--decor', nargs='?', default="t,i,e,s,se,lt", 
        help="decorator rules for result files. Default ''")

    parser.add_argument('-v', '--verbose', default="3,0", type=str, 
        help="Verbose level")
    
    usageOptions = parser.parse_args(args)
    usageOptions.curaction = ""
    usageOptions.lastaction = ""
    usageOptions.lastactions = []
    usageOptions.yesyes = True
    #usageOptions.grouplist = []
    usageOptions.groupcount = []
    usageOptions.filetype = ""
    usageOptions.actionlist = ['analyse', 'usage']
    usageOptions.yes = True
    usageOptions.configstr = ""
    usageOptions.copyexcel = 1
    nn1serv._initiate_folders(usageOptions, caller)
    usageOptions = nn1serv.initiate_externpath(usageOptions, withdialog=False)
    usageOptions = nn1serv.initiate_verbose(usageOptions)
    if isinstance(usageOptions.decor, str):
        usageOptions.decor = usageOptions.decor.split(",")
    usageOptions.decor = [val.strip() for val in usageOptions.decor]
    usageOptions.decor = nn1serv.decor2long(usageOptions.decor)
    if not usageOptions.usagedata:
        datafile = ""
    else:
        datafile = findFile(usageOptions.usagedata[0], ['~/docker', '~/docker/data', '~/docker/argsdir', '~/docker/result'])
    if isinstance(usageOptions.grouplist, str):
        usageOptions.grouplist = usageOptions.grouplist.split(',')
    if isinstance(usageOptions.usagedata, list) and bool(len(usageOptions.usagedata)):
        if os.path.isfile(datafile):
            usageOptions.source = datafile
            usageOptions.usagedata = ""
    else:
        if os.path.isfile(datafile):
            usageOptions.source = datafile
            usageOptions.usagedata = ""
    usageOptions, toprint, errorcode = nn1serv._initiate_debug(usageOptions)
    if hasattr(usageOptions, 'datafields') and isinstance(usageOptions.datafields, str):
        usageOptions.datafields = getListFromStr(usageOptions.datafields, double=True)
    
    return usageOptions

def usageInterne(cmd_line):
    internalFolder = '/home/docker/workdir'
    if not os.path.exists(internalFolder):
        internalFolder = '/Users/jeanluc/docker_work/Python3-Metaphor/metaphor-demo'
    if not len(cmd_line):
        print('need a command line')
        return
    
    iphenindex = len(cmd_line)
    for ind, val in enumerate(cmd_line):
        if val.startswith('-') and not isFloatEx(val):
            iphenindex = ind
            break

    hasdataline = '-d' in cmd_line
    index = -1
    if hasdataline:
        index = cmd_line.index('-d')
        data = cmd_line[index + 1]
        data = data.split(';')
    else:
        data = set2Float(cmd_line[:iphenindex])
        newdata = []
        ind = 0
        while ind < len(data) and isinstance(data[ind], str):
            newdata.append(data[ind])
            ind += 1
        if ind < len(data):
            lstst = [str(val) for val in data[ind:]]
            newdata.append(",".join(lstst))
#         data = newdata
        cmd_line = ["-d", ";".join(newdata)] + cmd_line[iphenindex:]
    if len(data) > 3:
        is_nn = True
    elif len(data) == 1:
        is_nn = isFloat(data[0])
    else:
        is_nn = isFloat(data[1])
    if is_nn:
        test = 'NN_'
    else:
        test = 'GM_'
    modelfile = ""
    for val in os.listdir(internalFolder):
        filetest = os.path.join(internalFolder, val)
        if os.path.isfile(filetest) and val.startswith(test) and val.endswith('.nnx'):
            modelfile = filetest
            break
    return usage([modelfile] + cmd_line)

def usage(cmd_line):
#     if DEBUG_USE:
#         print("usage command line\n\t{}".format(cmd_line))
    targetfile = os.path.expanduser("~/linkedServices.txt")
    with open(targetfile, 'w')  as ff:
        nn1serv.linkToServices(file=ff)
#     print("starting usage")
    iphenindex = len(cmd_line)
    for ind, val in enumerate(cmd_line):
        if val.startswith('-') and not isFloatEx(val):
            iphenindex = ind
            break
    cmd_line_start = cmd_line[:iphenindex]   
    cmd_line_end = cmd_line[iphenindex:]
    
    if not iphenindex:
        print("usage needs arguments")
        return
    
    modelfile = make_intern(cmd_line_start[0])
    mode = 'nn'
    hidden = 0
    if iphenindex:
        if modelfile.startswith('@'):
            argfile = modelfile[1:]
            print("fichier d'arguments : {}".format(argfile))
            print("Qu'en faire ?!?")
            return
        old = modelfile
        modelfile = findFile(modelfile, ['~/docker', '~/docker/data', '~/docker/argsdir', '~/docker/result'])
#         print("model file : {}".format(modelfile))
        if not modelfile:
            print("cannot open file : '{}'".format(old))
            return
        dico = getDictFromGmx(modelfile)
#         if not dico.get('xml', "") and not dico.get('modeldata', None):
        dicogene = dico.get('general', None)
        if dicogene and dicogene.get('grademax', 0):
            mode = 'gm'
        dicomodel = dico.get('model', None)
        if dicomodel:
            hidden = dicomodel.get('hidden', 0)       
    
    if len(cmd_line) < 2:
        print(dico)
    else:        
        usageOptions = getCommandLineUsageOptions(cmd_line_end)
        if not hasattr(usageOptions, 'propertyname') or not usageOptions.propertyname:
            usageOptions.propertyname = dico.get('propertyname', "")
        if not hasattr(usageOptions, 'test') and hasattr(usageOptions, 'source'):
            if os.path.exists(usageOptions.source):
                usageOptions.test = usageOptions.source
            if hasattr(usageOptions, 'datarange'):
                usageOptions.testrange = usageOptions.datarange 
            if hasattr(usageOptions, 'datafields'):
                usageOptions.testfields = usageOptions.datafields       
        if usageOptions.debug & DEMO_DEBUG_USAGE:
            print("usage command line\n\t{}".format(cmd_line))
        usageOptions.hidden = hidden
        usageOptions.mode = mode 
        data = ";".join(cmd_line_start[1:])
        nn1serv.usageAction(usageOptions, modelfile, data)

if __name__ == '__main__':
    usage(sys.argv[:1])