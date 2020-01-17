'''
Created on 4 févr. 2019

@author: jeanluc
'''
import sys

nobarverb = 3

USE_NO_LIB = 2

USE_PARALLEL = 1 #  !!! ATTENTION  !!!   remettre a 1
"""Use parallel processing when usefull
"""
USE_PARALLEL_COMPILE = USE_PARALLEL and 1  #  !!! ATTENTION  !!!
"""Use parallel processing for compiling models
"""
USE_PARALLEL_MODEL = USE_PARALLEL and 1  #  !!! ATTENTION  !!!
"""Use parallel processing for model sourcing
"""
USE_PARALLEL_MAIN = USE_PARALLEL and 1 # ici a remettre a 1
"""Use parallel processing  for main
"""
USE_PARALLEL_TEST = USE_PARALLEL and 1  # ici a remettre a 1
"""Use parallel processing for test
"""
USE_PARALLEL_LOO = USE_PARALLEL and 1  # ici a remettre a 1
"""Use parallel processing for LOO
"""
USE_PARALLEL_BS = USE_PARALLEL and 1  # ici a remettre a 1
"""Use parallel processing for BoosStrap
"""
USE_SUPER_TRAIN = 0
"""Use parallel processing for Super Train
"""
if not USE_PARALLEL:
    print("ATTENTION ======= no parallelism at all ======= ATTENTION", file=sys.stderr)
else:
    if not USE_PARALLEL_MAIN:
        print("ATTENTION ======= no main parallelism ======= ATTENTION", file=sys.stderr)
    if not USE_PARALLEL_COMPILE:
        print("ATTENTION ======= no compile parallelism ======= ATTENTION", file=sys.stderr)
    if not USE_PARALLEL_LOO:
        print("ATTENTION ======= no LOO parallelism ======= ATTENTION", file=sys.stderr)
    if not USE_PARALLEL_BS:
        print("ATTENTION ======= no Bootstrap parallelism ======= ATTENTION", file=sys.stderr)
    
USE_LIB_FOR_TEST = 0
"""Use library for test
"""