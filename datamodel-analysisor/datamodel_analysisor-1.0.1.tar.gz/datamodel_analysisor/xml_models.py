# coding:utf-8
"""
 FileName: xml_models.py
 Author: wangzp 
 CFFEX Confidential.
 
 @Copyright 2018 CFFEX.  All rights reserved. 
 The source code for this program is not published or otherwise divested of its trade secrets, 
 irrespective of what has been deposited with the China Copyright Office.
 
 Date:   2020-1-15 11:08
"""


class Float:
    def __init__(self, typename, length, precision, label):
        self.typename = typename
        self.length = length
        self.precision = precision
        self.label = label


class Int:
    def __init__(self, typename, length, label):
        self.typename = typename
        self.length = length
        self.label = label


class RangeInt:
    def __init__(self, typename, length, start, end, label):
        self.typename = typename
        self.length = length
        self.start = start
        self.end = end
        self.label = label


class Char:
    def __init__(self, typename, label):
        self.typename = typename
        self.label = label


class String:
    def __init__(self, typename, length, label):
        self.typename = typename
        self.length = length
        self.label = label


class EnumChar:
    def __init__(self, typename, label, prefix):
        self.typename = typename
        self.label = label
        self.prefix = prefix
        self.enum = {}

    def add(self, enum):
        self.enum[enum.name] = enum


class enum:
    def __init__(self, name, value, label):
        self.name = name
        self.value = value
        self.label = label


class UFDataTypes:
    def __init__(self):
        self.list_Float = {}
        self.list_Int = {}
        self.list_RangeInt = {}
        self.list_Char = {}
        self.list_EnumChar = {}
        self.list_String = {}
        self.field_type = {}


class EntityList:
    def __init__(self, list_entity):
        self.list_entity = list_entity

    def flatEntity(self, name):
        temp_children = {}
        for key in list(self.list_entity[name].child.keys()):
            ch = self.list_entity[name].child[key]
            if type(ch) is Field:
                temp_children[key] = ch
            if type(ch) is str:
                self.list_entity[name].child.pop(key)
                if key not in self.list_entity.keys():
                    return None
                self.flatEntity(self.list_entity[ch].name)
                for ke, sub_ch in self.list_entity[ch].child.items():
                    temp_children[ke] = sub_ch
        self.list_entity[name].child = temp_children

    def flat(self):
        for entity in self.list_entity.values():
            # print(entity.name)
            self.flatEntity(entity.name)


class Entity:
    def __init__(self, name, title, description):
        self.name = name
        self.title = title
        self.description = description
        self.child = {}

    def add(self, Field):
        self.child[Field.name] = Field

    def addRef(self, ref):
        self.child[ref] = ref

    def addEntity(self, Entity):
        for i in Entity.child:
            self.add(i)


class Field:
    def __init__(self, name, fildtype, description, notnull, label, iskey):
        self.name = name
        self.description = description
        self.type = fildtype
        self.notnull = notnull
        self.label = label
        self.iskey = iskey
