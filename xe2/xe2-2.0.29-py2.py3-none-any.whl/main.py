#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
# @copyright Copyright (C) Guichet Entreprises - All Rights Reserved
# 	All Rights Reserved.
# 	Unauthorized copying of this file, via any medium is strictly prohibited
# 	Dissemination of this information or reproduction of this material
# 	is strictly forbidden unless prior written permission is obtained
# 	from Guichet Entreprises.
###############################################################################

###############################################################################
# @package xenon2
###############################################################################

import logging
import sys
import os
import traceback
import argparse
import tempfile
import ctypes  # An included library with Python install.

import xe2
import xe2.inoutstream

__actions_list__ = {}
__actions_list__['generate_site'] = xe2.generate_site
__actions_list__['create_conf'] = xe2.create_conf


###############################################################################
# test the filename for argparsing
#
# @param filename The filename
# @return filename.
###############################################################################
def is_real_file(filename):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not os.path.isfile(filename):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} does not exist".format(filename))
    return filename

###############################################################################
# Create a windows message box
#
# @param text The message
# @param title The title of the windows
# @return nothing.
###############################################################################
def message_box(text, title):
    ctypes.windll.user32.MessageBoxW(0, text, title, 0)


###############################################################################
# Define the parsing of arguments of the command line
###############################################################################
def get_parser_for_command_line():
    docstring = ""
    for action in __actions_list__:
        docstring = docstring + action + ":\n" + \
            __actions_list__[action].__doc__.split("@")[0][0:-3] + "\n\n"

    description = \
        """This program generate a website.

""" + docstring

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--conf', dest="conf_filename", required=False,
                        type=is_real_file,
                        help="the configuration file in yaml", metavar="FILE")
    parser.add_argument('--gen-site', action='store', dest='gen_site',
                        choices=['yes', 'no'], default='no',
                        help='generate the website')
    parser.add_argument('--create-conf', dest="create_conf", required=False,
                        type=is_real_file,
                        help="Create the configuration from a md file",
                        metavar="FILE")
    parser.add_argument('--console', action='store_true', dest='console',
                        help='Set the output to the standard output '
                        'for console')
    parser.add_argument('--windows', action='store_true', dest='windows',
                        help='Define if we need all popups windows.')
    parser.add_argument('--verbose', action='store_true', dest='verbose',
                        help='Put the logging system on the console for info.')

    return parser

###############################################################################
# Find the filename of this file (depend on the frozen or not)
# This function return the filename of this script.
# The function is complex for the frozen system
#
# @return the filename of THIS script.
###############################################################################
def __get_this_filename():
    result = ""
    if getattr(sys, 'frozen', False):
        # frozen
        result = sys.executable
    else:
        # unfrozen
        result = __file__
    return result


###############################################################################
# Find the filename of this file (depend on the frozen or not)
# This function return the filename of this script.
# The function is complex for the frozen system
#
# @return the folder of THIS script.
###############################################################################
def __get_this_folder():
    return os.path.split(os.path.abspath(os.path.realpath(
        __get_this_filename())))[0]


###############################################################################
# Logging system
###############################################################################
def __set_logging_system():
    log_filename = os.path.splitext(os.path.abspath(
        os.path.realpath(__get_this_filename())))[0] + '.log'

    if xe2.inoutstream.is_frozen():
        log_filename = os.path.abspath(os.path.join(
            tempfile.gettempdir(),
            os.path.basename(__get_this_filename()) + '.log'))

    logging.basicConfig(filename=log_filename, level=logging.INFO,
                        format='%(asctime)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    console = logging.StreamHandler(xe2.inoutstream.initial_stream().stdout)
    console.setLevel(logging.INFO)

    # set a format which is simpler for console use
    formatter = logging.Formatter('%(asctime)s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger

    # if not xe2.inoutstream.is_frozen():
    logging.getLogger('').addHandler(console)

    return console

###############################################################################
# Main script
###############################################################################
def __main():
    console = __set_logging_system()
    # ------------------------------------
    logging.info('+')
    logging.info('-------------------------------------------------------->>')
    logging.info('Started %s', __get_this_filename())
    logging.info('The Python version is %s.%s.%s',
                 sys.version_info[0], sys.version_info[1], sys.version_info[2])

    try:
        parser = get_parser_for_command_line()
        logging.info("parsing args")
        args = parser.parse_args()
        logging.info("parsing done")

        if args.verbose == "yes":
            console.setLevel(logging.INFO)
        if args.console == "yes":
            xe2.inoutstream.initial_stream().apply_to_std_stream()
            if xe2.inoutstream.is_frozen():
                logging.getLogger('').addHandler(console)

        logging.info("conf_filename=%s", args.conf_filename)
        logging.info("gen_site=%s", args.gen_site)
        logging.info("create_conf=%s", args.create_conf)
        logging.info("verbose=%s", args.verbose)

        args.gen_site_bool = (args.gen_site == "yes")

        conf_filename = args.conf_filename

        if args.create_conf is not None:
            conf_filename = xe2.create_conf(args.create_conf)

        if args.gen_site_bool:
            xe2.generate_site(conf_filename)

    except argparse.ArgumentError as errmsg:
        logging.error(str(errmsg))
        if ('args' in locals()) and (args.windows):
            message_box(text=parser.format_usage(), title='Usage')

    except SystemExit:
        if ('args' in locals()) and (args.windows):
            message_box(text=parser.format_help(), title='Help')

    except Exception as ex:
        logging.error(str(ex))
        if ('args' in locals()) and (args.windows):
            message_box(text=str(ex), title='Usage')

    except:
        var = traceback.format_exc()
        logging.error('Unknown error : \n %s', var)
        if ('args' in locals()) and (args.windows):
            message_box(text='Unknown error : \n' + var,
                        title='Error in this program')
        # raise

    logging.info('Finished')
    logging.info('<<--------------------------------------------------------')
    logging.info('+')
    # ------------------------------------


# -----------------------------------------------------------------------------
# Call main if the script is main
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    __main()
