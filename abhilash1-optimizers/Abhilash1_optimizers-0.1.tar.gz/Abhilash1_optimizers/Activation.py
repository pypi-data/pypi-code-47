# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 12:39:41 2019

@author: 45063883
"""

import math
import numpy as np

class Activation():
    def sigmoid(x):
        return (1.0/(1.0 + math.exp(-x)))
    def relu(x):
        return max(x,0)
    def elu(x,alp):
        if x<=0:
            return alp*(math.exp(x)-1)
        elif x>0:
            return x
    def selu(scale,x,alp):
        return scale*Activation.elu(x,alp)
    def tanh(x):
        return ((math.exp(x)-math.exp(-x))/(math.exp(x)+math.exp(-x)))
    def hard_sigmoid(x):
        if x>2.5:
            return 1
        elif x<(-2.5):
            return 0
        elif(x>=(-2.5) and x<=(2.5)):
            return (0.2*x +0.5)
    def exponential(x):
        return math.exp(x)
    def linear(x):
        return x
    def softsign(x):
        return (1.0/math.abs(x)+1.0)
    def softplus(x):
        return math.log(math.exp(x)+1)

    