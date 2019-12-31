#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Le référentiel d'information de Guichet Entreprises est mis à disposition
# selon les termes de la licence Creative Commons Attribution - Pas de
# Modification 4.0 International.

# Pour accéder à une copie de cette licence, merci de vous rendre à l'adresse
# suivante :
# http://creativecommons.org/licenses/by-nd/4.0/
# ou envoyez un courrier à Creative Commons, 444 Castro Street, Suite 900,
# Mountain View, California, 94041, USA.
# -----------------------------------------------------------------------------

import logging
import sys
import os
import treelib

if (__package__ in [None, '']) and ('.' not in __name__):
    import ref
else:
    from . import ref


##############################################################################
# An object to manipulate le referential folder tree
# -----------------------------------------------------------------------------
class ReferentialFolderTree():

    ###########################################################################
    # Initialize the object from a pattern of folder name
    #
    # @param root the root folder
    # @param pattern the pattern to print the folder
    # @param order_list the order of the folder level
    # @param lang the language
    ###########################################################################
    def __init__(self, root=None,
                 pattern=None,
                 order_list=None,
                 lang=None):

        # set the first value
        self.__tree = treelib.Tree()
        self.__root = root
        __pattern = pattern
        __order_list = order_list

        self.__tree.create_node(tag='root', identifier='Root')
        if __pattern is None:
            __pattern = {'category': "%(category-ascii)s",
                         'name': "%(name-ascii)s",
                         'domain': "%(domain-ascii)s",
                         'lang': "%(lang)s"}

        if __order_list is None:
            __order_list = ['category', 'domain', 'name']

        for key in ref.get_info_ref():
            for lang_it in ref.get_info_ref()[key]:
                if lang_it in ['path', 'filename', 'src']:
                    continue
                # if lang is not None and
                local_data = ref.get_info_ref()[key][lang_it]
                node_id = self.__tree.root

                for keyword in __order_list:
                    # for x in local_data:
                    #     print(x)
                    # print(local_data)
                    tag = __pattern[keyword] % local_data
                    children = self.__tree.children(node_id)
                    found_child_id = None
                    for child in children:
                        if child.tag == tag:
                            found_child_id = child.identifier
                            break
                    if found_child_id is None:
                        found_child_id = self.__tree.create_node(
                            tag=tag,
                            data=local_data,
                            parent=node_id).identifier
                    node_id = found_child_id

    ###########################################################################
    # the tree of the folder
    # @return the value
    ###########################################################################
    @property
    def tree(self):
        return self.__tree

    ###########################################################################
    # the root of the folder
    # @return the value
    ###########################################################################
    @property
    def root(self):
        return self.__root

    ###########################################################################
    # the root of the folder
    # @param value The value to set
    ###########################################################################
    @root.setter
    def root(self, value):
        self.__root = value


# -----------------------------------------------------------------------------
# Find the filename of this file (depend on the frozen or not)
# This function return the filename of this script.
# The function is complex for the frozen system
#
# @return the filename of THIS script.
# -----------------------------------------------------------------------------
def __get_this_filename():
    result = ""

    if getattr(sys, 'frozen', False):
        # frozen
        result = sys.executable
    else:
        # unfrozen
        result = __file__

    return result

# -----------------------------------------------------------------------------
# Set up the logging system
# -----------------------------------------------------------------------------
def __set_logging_system():
    log_filename = os.path.splitext(os.path.abspath(
        os.path.realpath(__get_this_filename())))[0] + '.log'
    logging.basicConfig(filename=log_filename, level=logging.DEBUG,
                        format='%(asctime)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(asctime)s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)


# -----------------------------------------------------------------------------
# Launch the test
# -----------------------------------------------------------------------------
def __launch_test():
    import pytest
    pytest.main(__get_this_filename())

# -----------------------------------------------------------------------------
# Main script call only if this script is runned directly
# -----------------------------------------------------------------------------
def __main():
    # ------------------------------------
    logging.info('Started %s', __get_this_filename())
    logging.info('The Python version is %s.%s.%s',
                 sys.version_info[0], sys.version_info[1], sys.version_info[2])

    folders = ReferentialFolderTree(
        pattern={'category': "%(category-expand-ascii)s",
                 'domain': "%(domain-filename-short)s",
                 'name': "%(key)s - %(name-filename-short)s",
                 'lang': "%(lang)s"},
        order_list=['category', 'domain', 'name'])
    print(folders.tree)

    # folders.root = r"C:\dev\projet-ge.fr\informations\reference"

    logging.info('Finished')
    # ------------------------------------


# -----------------------------------------------------------------------------
# Call main function if the script is main
# Exec only if this script is runned directly
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    __set_logging_system()
    __main()
