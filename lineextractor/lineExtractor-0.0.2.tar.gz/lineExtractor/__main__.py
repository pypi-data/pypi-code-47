#!/usr/bin/env python

# lineExtractor.py
__version__ = "0.0.2"

import sys
import getopt

def main():    
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'b:c:e:hit', ['begins=', 'contains=', 'ends=', 'help', 'trim', 'insensitive'])
    except getopt.GetoptError:
        error_response("Error in parsing command line arguments")
        sys.exit(2)

    # Used to track the number of non required arguments
    num_option_args = 0
    # Maps condition phrases to condition check functions
    conditions_dict = {}
    # List of alteration functions
    alterations = []
    for opt, arg in options:
        num_option_args += 1
        if arg is not None:
            num_option_args += 1

        if opt in ('-b', '--begins'):
            conditions_dict[arg] = check_begins
        if opt in ('-c', '--contains'):
            conditions_dict[arg] = check_contains
        if opt in ('-e', '--ends'):
            conditions_dict[arg] = check_ends
        if opt in ('-h', '--help'):
            print_help()
            sys.exit(0)
        if opt in ('-i', '--insensitive'):
            alterations.append(caseInsensitive)
        if opt in ('-t', '--trim'):
            alterations.append(trim_line)

    # Check for src_file dest_file arguments
    if len(sys.argv) - 1 - num_option_args != 2:
        error_response('You must specify a pair input and output files')
        sys.exit(1)

    src_file = ''
    dest_file = ''

    try:
        src_file = open(sys.argv[-2])
    except IOError as identifier:
        error_response('Unable to open source file ' + sys.argv[1])
        sys.exit(1)

    try:
        dest_file = open(sys.argv[-1], 'w')
    except IOError as identifier:
        error_response('Unable to open destination file ' + sys.argv[2])
        sys.exit(1)

    # Apply alterations to the dictionary of conditions
    altered_conditions_dict = {}
    for condition in conditions_dict:
        altered_condition = apply_alterations(condition, alterations)
        altered_conditions_dict[altered_condition] = conditions_dict[condition]
    
    evaluate_lines(src_file, dest_file, altered_conditions_dict, alterations)


def evaluate_lines(src_file, dest_file, conditions, alterations):
    check_functions = [check_begins, check_contains, check_ends]

    for line in src_file:
        test_line = apply_alterations(line, alterations)
        passes = True
        for condition in conditions:
            if condition is not None:
                check = conditions[condition]
                passes = passes and check(test_line, condition)
        if passes:
            dest_file.write(line)

def check_begins(line, phrase):
    if line.startswith(phrase):
        return True
    return False

def check_contains(line, phrase):
    if phrase in line:
        return True
    return False

def check_ends(line, phrase):
    if line.endswith(phrase):
        return True
    return False

def apply_alterations(line, alterations):
    for alteration in alterations:
        line = alteration(line)
    return line

def trim_line(line):
    return line.strip()

def caseInsensitive(line):
    return line.lower()

def print_help():
    title = ''' 
  _     _              _____      _                  _             
 | |   (_)_ __   ___  | ____|_  _| |_ _ __ __ _  ___| |_ ___  _ __ 
 | |   | | '_ \ / _ \ |  _| \ \/ / __| '__/ _` |/ __| __/ _ \| '__|
 | |___| | | | |  __/ | |___ >  <| |_| | | (_| | (__| || (_) | |   
 |_____|_|_| |_|\___| |_____/_/\_\\__|_|  \__,_|\___|\__\___/|_|   
                                                                   
    '''
    print(title)
    print('This tool is meant to analyze an input file and extract particular lines to an output file.')
    print('I made this tool to help myself analyze microservice logs if it helps you or you would like to suggest changes the link to the Github Repo is: https://github.com/kvanland/lineExtractor/')
    print('\n')
    print('Usage:')
    print('lineExtractor [Options] input.txt output.txt ')
    print('Note: Multiple options will result in an AND of the options (e.g. if you select begins foo and contains bar you will get only lines that begin with foo AND contain bar.)')
    print('\n')
    print('Options:')
    print('-b --begins=<target-phrase>   If a line in the input file begins with <target-phrase> it will be written to the output file')
    print('-c --contains=<target-phrase> If a line in the input file contains <target-phrase> it will be written to the output file')
    print('-e --ends=<target-phrase>     If a line in the input file ends with <target-phrase> it will be written to the output file')
    print('-h --help                     Prints this output')
    print('-t --trim                     Trims whitespace from both the optional phrases from -b, -c, and -e as well as each line when evaluating')
    print('-i --insensitive              Converts all optional phrases from -b, -c, and -e as well as each line to lower case when evaluating')

def error_response(msg):
    print(msg)
    print('For more information please use the --help option')
    
if __name__=='__main__':
    main()