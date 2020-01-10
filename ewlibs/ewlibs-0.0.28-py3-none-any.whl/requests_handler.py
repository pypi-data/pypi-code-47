import requests
import json
import sys
import os
sys.path.append(os.getcwd())
from ewlibs.jsonp_handler import loads_jsonp

convert_dic = {
    "json": json.loads,
    "jsonp": loads_jsonp,
}


def data_convert(format="json"):
    def decorator(fn):
        def objectMethod(c_url, r_data=None, *args, **kwargs):
            #处理业务
            fn(c_url=c_url,
               r_data=convert_dic[format](r_data),
               *args,
               **kwargs)

        return objectMethod

    return decorator


def crawl_data():
    def decorator(fn):
        def objectMethod(c_url, r_data=None, *args, **kwargs):
            r = requests.get(c_url)
            #处理业务
            fn(c_url=c_url, r_data=r.text, *args, **kwargs)

        return objectMethod

    return decorator