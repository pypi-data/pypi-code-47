# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:34:20 2019

@author: LP885RH
"""

def unique(list1): 
    
    # intilize a null list 
    unique_list = [] 
    index_list = []
    # traverse for all elements 
    for i, x in enumerate(list1):  
        # check if exists in unique_list or not 
        if (x.source, x.table) not in unique_list:
            unique_list.append((x.source, x.table))
            index_list.append(i)
    return index_list


def get_tables(list1):
    index = unique(list1)
    return [list1[i] for i in index]

def isnan(num):
    return num != num