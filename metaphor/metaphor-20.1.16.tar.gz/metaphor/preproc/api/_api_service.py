'''
Created on 20 févr. 2019

@author: jeanluc
metaphor.preproc.api._api_service
'''

from ...nntoolbox.utils import doNothing
from ...nntoolbox.cmd_line_dialogs import choiceQuestion, \
    valueQuestion, yesNoQuestion, chooseFields
from ...nn1.api._api_service import dialogdefaults
from ...preproc.preproc_engine import _preprocAction, preproctypelist, preprocdefaults

modulesticker = "PP"

fullpreproctypelist = preproctypelist + list(range(len(preproctypelist)))

help1="""Preproc type: 
    '' -> none, 
    'repartition' -> random probe linear function', 
    'normal -> random probe with linear + crossd-product' 
    'full -> random probe with full 2nd order'"""
arg1 = ('-pp', '--preproctype', str, "linear",fullpreproctypelist, "dico",
    help1)

help2 = "Number of random probe initialization. Default 1000"
arg2 = ('-pc', '--probecount', int, 1000, fullpreproctypelist, "dico", 
    help2)

add_arg_list = [arg1, arg2]

def preProcAction(options, doprint=doNothing, forcedefault=False):
    """Input data selection with the random probe method.
    
    Arguments:
     - options -> options namespace.
     - doprint -> print function
     - forcedefault -> force the action without question.
     
    Following the action, the data selection in options may be changed
    """
    if not 'preproc' in options.actionlist or not 'inputs' in options.grouplist:
        return
    mess = "do you want to perform inputs relevance analysis"
    valdef = int(dialogdefaults['preproc']['dopreproc'])
    accept = yesNoQuestion(mess, default=valdef, doprint=doprint, 
                           forcedefault=forcedefault)
    if accept:           
        getout = False
        doprint("running input selection")
        curyes = options.yes
        options.yes = False
        try:
            preprocres = _preprocAction(options, doprint)
            if preprocres is not None:
                options = preprocres
            else:
                getout = True
        except Exception as err:
            doprint(err)
            getout = True
        finally:
            options.yes = curyes
            doprint('api input selection done')
        if getout:
            return -1
    return 0 
