import re
from operator import and_
from datetime import datetime
from functools import reduce

from sqlalchemy import create_engine, Column, Table, MetaData, Text, BigInteger, DateTime
from sqlalchemy.pool import NullPool
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import sql

from .enums import *

__all__ = [
    'parse_arn',
    'primary_key_stmt',
    'image_as_item'
]

arn_regex = re.compile(r'arn:aws:dynamodb:(?P<region>.*?):(?P<account_id>.*?):table/(?P<table>.*?)/.*')

def parse_arn(arn):
    return arn_regex.match(arn).groupdict()

def primary_key_stmt(keys, table):
    """combine the individual equalities incase of composite primary keys"""
    return reduce(and_, [table.c.get(key) == value for key, value in keys.items()])

def default_columns():
    return [
        Column('item', JSONB),
        Column('mod_time', DateTime, default=datetime.now, onupdate=datetime.now),
        Column('create_time', DateTime, default=datetime.now)
    ]

def table_columns(keys):
    # TODO: Non text primary keys?
    columns = [Column(key['AttributeName'], Text, primary_key=True) for key in keys] + default_columns()
    return columns


def image_as_item(image):

    item = {}

    for column_name, field in image.items():
        data_type, value = next(iter(field.items()))

        if data_type == DataType.number:
            try:
                value = int(value)
            except ValueError:
                value = float(value)

        elif data_type == DataType.string:
            pass
        else:
            print('Unhandled data type')
            try:
                json.dumps(value)
            except:
                value = str(value)

        item[column_name] = value

    return item
