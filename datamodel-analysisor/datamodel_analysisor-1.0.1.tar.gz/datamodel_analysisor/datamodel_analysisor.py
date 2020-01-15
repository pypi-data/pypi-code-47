# coding:utf-8
"""
 FileName: main.py
 Author: wangzp 
 CFFEX Confidential.
 
 @Copyright 2018 CFFEX.  All rights reserved. 
 The source code for this program is not published or otherwise divested of its trade secrets, 
 irrespective of what has been deposited with the China Copyright Office.
 
 Date:   2020-1-15 10:39
"""
import os
import re
import codecs
import xml.etree.ElementTree as et
from xml_models import *


class api_method(type):
    def get_real_type(cls, model, name):
        pass

    def get_real_value(cls, model, name, value):
        pass


class analysisor(metaclass=api_method):
    def __init__(self, root_path):
        self.init_xml = InitXml(root_path)
        self.create_hash()

    def create_hash(self):
        pass

    def get_real_type(self, model, name):
        field = self.init_xml.entity_tree[model].child[name].type
        return self.init_xml.ufdata_tree.field_type[field]

    def get_real_value(self, model, name, value):
        return self.get_real_type(model, name)(value)


class InitXml:
    def __init__(self, root_path):
        self.root_path = root_path
        self.Entity_old = os.path.join(root_path, "UFEntity.xml")
        self.Entity_new = os.path.join(root_path, "new_UFEntity.xml")
        self.UFData_old = os.path.join(root_path, "UFDataType.xml")
        self.UFData_new = os.path.join(root_path, "new_UFDataType.xml")

        self.trans_codecs(self.Entity_old, self.Entity_new)
        self.trans_codecs(self.UFData_old, self.UFData_new)

        self.entity_tree = UFEntityAnalysisor(self.Entity_new).get_flat_entity()
        self.ufdata_tree = UFDataAnalysisor(self.UFData_new).get_types()

    def trans_codecs(self, filepath, new_filepath):
        with open(filepath, 'r') as f:
            content = f.read()
            content = re.sub("gb2312", "UTF-8", content)
        with open(new_filepath, 'w') as f:
            f.write(content)
        with codecs.open(new_filepath, 'rb', 'mbcs') as f:
            text = f.read().encode('utf-8')
        with open(new_filepath, 'wb') as f:
            f.write(text)


class UFEntityAnalysisor:
    def __init__(self, ufentity_file):
        self.ufentity_file = ufentity_file
        self.tree = et.parse(self.ufentity_file)
        self.root = self.tree.getroot()
        self.dict_entity = {}
        self.entity_list = None

    def analysis(self):
        for entity in self.root.findall("Entity"):
            temp = Entity(entity.get('name'), entity.get('title'), entity.get('description'))
            try:
                # print("----------")
                # print(entity.get("name"))
                for i in entity.findall('Field'):
                    # print(i.get('name'), i.get('type'), i.get('description'), i.get('notnull'), i.get('label'), i.get('iskey'))
                    temp.add(Field(i.get('name'), i.get('type'), i.get('description'), i.get('notnull'), i.get('label'), i.get('iskey')))
                for i in entity.findall('Ref'):
                    temp.addRef(i.get('entity'))
            except:
                # print("pass")
                pass
            self.dict_entity[temp.name] = temp
        return self.dict_entity

    def get_flat_entity(self):
        self.entity_list = EntityList(self.analysis())
        self.entity_list.flat()
        return self.entity_list.list_entity


class UFDataAnalysisor:

    def __init__(self, ufdata_file):
        self.ufdata_file = ufdata_file
        self.tree = et.parse(self.ufdata_file)
        self.root = self.tree.getroot()
        self.datatypes = UFDataTypes()

    def get_types(self):
        for enumchar in self.root.findall("EnumChar"):
            temp = EnumChar(enumchar.get("typename"), enumchar.get("label"), enumchar.get("prefix"))
            for i in enumchar:
                temp.enum[i.get("name")] = enum(i.get("name"), i.get("value"), i.get("label"))
                self.datatypes.list_EnumChar[temp.typename] = temp
                self.datatypes.field_type[temp.typename] = str

        for string in self.root.findall("String"):
            temp = String(string.get("typename"), string.get("length"), string.get("label"))
            self.datatypes.list_String[temp.typename] = temp
            self.datatypes.field_type[temp.typename] = str

        for char in self.root.findall("Char"):
            temp = Char(char.get("typename"), char.get("label"))
            self.datatypes.list_Char[temp.typename] = temp
            self.datatypes.field_type[temp.typename] = str

        for int_ in self.root.findall("Int"):
            temp = Int(int_.get("typename"), int_.get("length"), int_.get("label"))
            self.datatypes.list_Int[temp.typename] = temp
            self.datatypes.field_type[temp.typename] = int

        for float_ in self.root.findall("Float"):
            # print("1")
            temp = Float(float_.get("typename"), float_.get("length"), float_.get("precision"), float_.get("label"))
            self.datatypes.list_Float[temp.typename] = temp
            self.datatypes.field_type[temp.typename] = float

        for rangeint in self.root.findall("RangeInt"):
            # print("1")
            temp = RangeInt(rangeint.get("typename"), rangeint.get("length"), rangeint.get("from_"), rangeint.get("to_"),
                            rangeint.get("label"))
            self.datatypes.list_RangeInt[temp.typename] = temp
            self.datatypes.field_type[temp.typename] = int
        return self.datatypes


