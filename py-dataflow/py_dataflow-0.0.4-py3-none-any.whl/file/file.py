# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, json
from datetime import datetime
from model.broker_enum import OperationEnum, TypeOrderEnum, TypeMethod, JobStatusEnum, TypeTradeEnum
from utils import dt_util


"""
###########################################################################
                   get and find file dir_local
###########################################################################
"""
def remove_files_path(type_file='*'):
    """
    :param _file_name:
    :return:
    """
    for file in get_all_files(type_file):
        os.remove(file[1])

def try_get_file_local(pattern='*'):
    """
    :return: time of 10 seconds to found file
    """
    cont_max_try = 50
    cont_tp = 0
    # import ipdb; ipdb.set_trace()
    while cont_tp <= cont_max_try:
        path_file = get_all_files(pattern= pattern)
        if path_file:
            return path_file[0][1]        # get first file local
        else:
            time.sleep(0.2)
            cont_tp += 1

def get_all_files(pattern='*', path=None):
    """
    :param path:
    :param pattern:
    :return: os.walk(path): return 3 variaveis
    """
    datafiles = []
    path = path or settings.DIR_LOCAL
    for root,dirs,files in os.walk(path):
        for file in fnmatch.filter(files, pattern):
            pathname = os.path.join(root, file)
            filesize = os.stat(pathname).st_size
            datafiles.append([file, pathname, filesize])
    if len(datafiles) > 0:
        return datafiles
    else:
        return []