#!/usr/bin/env python2
from __future__ import print_function

import numpy

dt = numpy.dtype({'names':['a','b','c','d','e'], 'formats':[float,float,float,float,float]})

a = numpy.zeros([5], dtype=dt)
a['a'] = 1
a['b'] = 2
a['c'] = 3
a['d'] = 4
a['e'] = 5

print(a)
print(a[['a','b','c']])
print(a[['a','b','c']].view(float))
