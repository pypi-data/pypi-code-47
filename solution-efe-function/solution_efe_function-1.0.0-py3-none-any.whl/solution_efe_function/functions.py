import random
import string
import math

def getCodeMail(length):
    key = ''
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    codeArray = random.sample(list, 6)
    for nro in codeArray:
        key += str(nro)
    return key

def paramsBodyValid(params,bodyJson):
    paramsValid = True
    for param in params:
        if (param not in bodyJson):
            paramsValid = False
            break
    return paramsValid

def paramsQueryValid(params,bodyJson):
    paramsValid = True
    for param in params:
        if (param not in bodyJson):
            paramsValid = False
            break
    return paramsValid

def randomString(stringLength=64):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def countPage(countRecord,limit):
    reciduo=countRecord%limit
    if reciduo==0:
        return math.trunc(countRecord/limit)
    else:
        return math.trunc(countRecord/limit) +1

def getTokenHeader(header):
    headers = header.split()
    return headers[1]