# -*- coding: utf-8 -*-
"""Main module for running ``make`` targets with minimal
effort command-line invokation.

Module Description
==================

Main module that relies on :class:`argparse.Namespace` to relay parameters
for running the application.

.. moduleauthor:: David Grethlein <djg329@drexel.edu>`

Module Contents
===============

"""

import os
import sys
import json
import argparse

#==============================================================================
#		ARG-PARSE SET-UP
#==============================================================================
TOP_LEVEL_DESCRIPTION = "Rubix Cube Package Argument Parser"

# Argument parser for direct command line interaction
parser = argparse.ArgumentParser(description=TOP_LEVEL_DESCRIPTION)
subparsers = parser.add_subparsers(help=' {----- Package Command(s)  -----}')

#------------------------------------------------
#	TEST RUBIX CUBE PARSER 
#------------------------------------------------
test_cube_parser = subparsers.add_parser('test_cube',
	help='Generates a solved 3x3 Rubix Cube object.')


#==============================================================================
#		PARSE ARGUMENTS
#==============================================================================
# Parse arguments
args = parser.parse_args()
if len(vars(args)) > 0:
	args.func(args)