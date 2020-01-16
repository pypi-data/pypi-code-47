# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 09:54:17 2019

@author: LP885RH
"""

class Element(object):
    def __init__(self, source, table, route, table_alias, table_description, field, 
                 alias, description, BusinessTerm, Attributes):
        self.source = source
        self.table = table
        self.route = route
        self.table_alias = table_alias
        self.table_description = table_description
        self.field = field
        self.alias = alias
        self.description = description
        self.BusinessTerm = BusinessTerm
        self.Attributes = Attributes

class QR_object(object):
    def __init__(self, source, table, route, name, description, column, condition, value, 
                 check_type, check_op, check_val, action, status):
        
        self.source = source
        self.table = table
        self.route = route
        self.name = name
        self.description = description
        self.column = column
        self.condition = condition
        self.value = value
        self.check_type = check_type
        self.check_op = check_op
        self.check_val = check_val
        self.action = action
        self.status = status

class Attributes(object):
    def __init__(self, data_owner, data_origin, nullable, quality_rule):
        self.data_owner = ('Data owner', data_owner)
        self.data_origin = ('Data origin', data_origin)
        self.nullable = ('Nullable', nullable)
        self.quality_rule = ('Quality Rule', quality_rule)

class BusinessTerm(object):
    def __init__(self, community, domain, data_point):
        self.community = community
        self.domain = domain
        self.data_point = data_point

        
        
    
        