# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#  from swat.wdggenerator import genwdg, overlapping_fractional_slot_slayer, overlapping_fractional_slot_dlayer
from swat_em.wdggenerator import genwdg
from swat_em.wdggenerator import winding_from_general_equation
from swat_em.datamodel import datamodel
#  import swat_em.analyse
import numpy as np
import pdb



print('Test double layer toothcoilwinding')
Q = 18
p = 8
m = 3
wstep = 1
layers = 2
#  U = [[1, -2, 3, 10, -11, 12], [-2, 3, -4, -11, 12, -13]]
#  V = [[4, -5, 6, 13, -14, 15], [-5, 6, -7, -14, 15, -16]]
#  W = [[7, -8, 9, 16, -17, 18], [-8, 9, -10, -17, 18, -1]]
#  U = [[1,  8, -9, 10, 17, -18], [-2, -9, 10, -11, -18, 1]]
#  V = [[2, -3, 4, 11, -12, 13], [-3, 4, -5, -12, 13, -14]]
#  W = [[5, -6, 7, 14, -15, 16], [-6, 7, -8, -15, 16, -17]]
kw1 = 0.9452		
kw5 = -0.1398		
kw7 = -0.0607
ret = winding_from_general_equation(Q, 2*p, m, wstep, layers)
wdglayout = ret['phases']
print(wdglayout)
#  assert [U, V, W] == wdglayout


data = datamodel()
#  data.set_config(get_init_config())
data.set_machinedata(Q = Q, p = p, m = m)
data.set_phases(wdglayout)
data.set_windingstep(wstep)
data.analyse_wdg()

idx = data.results['nu_el'].index(1)
#  assert kw1 == np.round(data.results['kw_el'][idx][0], 4) # phase U
#  assert kw1 == np.round(data.results['kw_el'][idx][1], 4) # phase V
#  assert kw1 == np.round(data.results['kw_el'][idx][2], 4) # phase W
idx = data.results['nu_el'].index(5)
#  assert kw5 == np.round(data.results['kw_el'][idx][0], 4) # phase U
#  assert kw5 == np.round(data.results['kw_el'][idx][1], 4) # phase V
#  assert kw5 == np.round(data.results['kw_el'][idx][2], 4) # phase W
idx = data.results['nu_el'].index(7)
#  assert kw7 == np.round(data.results['kw_el'][idx][0], 4) # phase U
#  assert kw7 == np.round(data.results['kw_el'][idx][1], 4) # phase V
#  assert kw7 == np.round(data.results['kw_el'][idx][2], 4) # phase W

bc, txt = data.get_basic_characteristics()
print(bc)
data.save_to_file('18-16.wdg')
