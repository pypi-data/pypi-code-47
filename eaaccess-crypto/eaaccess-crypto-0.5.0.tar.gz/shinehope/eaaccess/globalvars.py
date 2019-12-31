# Global Vars and Functions shared in mutiprocessing
from multiprocessing import Value
import datetime

__GlobalVars__ = {}

def GlobalVarSet(keyname:str, value: float) -> datetime.datetime:
    global  __GlobalVars__

    v = Value('d', value)
    __GlobalVars__[keyname] = v

    return  datetime.datetime.now()

def GlobalVarGet(keyname:str) ->  float:
    if __GlobalVars__[keyname]:
        v: Value = __GlobalVars__[keyname]
        return v.value
    else:
        return 0

def GlobalVarDel(keyname:str) -> bool:
    try:
        del __GlobalVars__[keyname]
        return  True
    except:
        return  False