import os
'''-----------------------------------------------------------------------------
DIRECTORIES AND FILES
-----------------------------------------------------------------------------'''
MODULE_DIR      = os.path.dirname(os.path.realpath(__file__))
PY_PROJECT_DIR  = os.path.join(MODULE_DIR, '..')
PROJECT_DIR     = os.path.join(PY_PROJECT_DIR, '..')

DATA_DIR        = os.path.join(PROJECT_DIR, 'data')
MODELS_DIR      = os.path.join(PROJECT_DIR, 'models')
NOTEBOOKS_DIR   = os.path.join(PROJECT_DIR, 'notebooks')
EXPERIMENTS_DIR = os.path.join(PROJECT_DIR, 'experiments')
