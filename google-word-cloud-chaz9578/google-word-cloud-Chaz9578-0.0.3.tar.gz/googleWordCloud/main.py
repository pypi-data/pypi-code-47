#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 21:47:00 2018

@author: charlie.plumley
"""


from google_word_cloud import googleWordCloud


if __name__ == '__main__':
    
    searchTerm = 'resilience'
    
    googleWordCloud(searchTerm)


