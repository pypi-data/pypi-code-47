# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 12:56:21 2019

@author: 45063883
"""

import math
import numpy as np

class hyperparameter():
    def initialise(alpha,first_moment,second_moment,epsilon,noise_g):
        return alpha,first_moment,second_moment,epsilon,noise_g