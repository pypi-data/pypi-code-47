#coding=utf8
from uliweb import expose, functions

@expose('/favicon.ico')
def favicon():
    return redirect('/static/favicon.ico')
