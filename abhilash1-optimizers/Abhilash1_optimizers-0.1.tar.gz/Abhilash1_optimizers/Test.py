# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:20:24 2019

@author: 45063883
"""

import Abhilash1_optimizers.ADAM_modified_update as ad

if __name__=="__main__":
    s=[0.8,0.9,0.7,0.67]
    max_itr=5
    ad.ADAMM.initialize(s,max_itr)