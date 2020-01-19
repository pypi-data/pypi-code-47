# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, json
from datetime import datetime, date
from decimal import Decimal
from sanic import response


class JsonEncoder(json.JSONEncoder):
    """Supports date and decimal objects"""

    def default(self, value):
        if isinstance(value, date):
            return value.strftime("%Y-%m-%d")
        if isinstance(value, Decimal):
            return float(value)
        return super(JsonEncoder, self).default(value)


def json_response(data):
    return response.json(data, dumps=json.dumps, cls=JsonEncoder, ensure_ascii=False)


def jsonToDF(spark, json=[], json_file=""):
    # content = None
    if isfile(json_file):
        content = spark.sparkContext.wholeTextFiles(json_file).values()
    else:
        # json = str(json).replace("b\'[", "").replace("\']","")
        json = [str(json).replace("None", "null")]
        context = spark.sparkContext.parallelize(json)
    return spark.read.json(context)


def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())


def serialize(_json):
    _serialize = json.loads(json.dumps(_json.__dict__))
    return _serialize


def json2obj(data):
    _json = strToJson(data)
    _object = json.loads(_json, object_hook=_json_object_hook)
    return _object


def strToJson(data)
    _json = json.dumps(data)
    return _json