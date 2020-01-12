#!/usr/bin/env python

##  demo.py

##  Please read the Introduction to the ComputationalGraphPrimer module to understand what
##  this script is trying to demonstrate.  The main purpose of the ComputationalGraphPrimer
##  module is for it to serve as a stepping stone to understanding automatic
##  calculation of the partial derivatives and loss gradients in modern Python based
##  deep learning frameworks like PyTorch.


import random

seed = 0           
random.seed(seed)

from ComputationalGraphPrimer import *

cgp = ComputationalGraphPrimer(
               expressions = ['xx=xa^2', 
                              'xy=ab*xx+ac*xa', 
                              'xz=bc*xx+xy', 
                              'xw=cd*xx+xz^3'],
               output_vars = ['xw'],
               dataset_size = 10000,
               learning_rate = 1e-6,
               display_vals_how_often = 1000,
               grad_delta = 1e-4,
      )

cgp.parse_expressions()

#cgp.display_network1()
cgp.display_network2()

cgp.gen_gt_dataset(vals_for_learnable_params = {'ab':1.0, 'bc':2.0, 'cd':3.0, 'ac':4.0})

cgp.train_on_all_data()

cgp.plot_loss()

