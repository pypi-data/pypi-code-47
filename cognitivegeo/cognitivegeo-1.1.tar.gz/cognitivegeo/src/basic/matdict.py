#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     March 2018                                                                      #
#                                                                                           #
#############################################################################################

# basic functions for processing python dictionary

import sys, os
import numpy as np
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.vis.messager import messager as vis_msg


__all__ = ['matdict']


def isDictConstantRow(dict):
    """
    Check if the dictionary has the same number of rows in all keys

    Args:
        dict:   Matrix dictionary

    Returns:
        True or false
    """

    # Check if the input dictionary be empty
    if len(dict.keys()) <= 0:
        vis_msg.print('ERROR in isDictConstantRow: Empty dictionary', type='error')
        sys.exit()

    firstkey = list(dict.keys())[0]
    nrow = len(dict[firstkey])

    for key in dict.keys():
        if nrow != len(dict[key]):
            vis_msg.print('ERROR in isDictConstantRow: ' + key + ' of inconstant row number',
                          type='error')
            return False

    return True


def maxDictConstantRow(dict):
    """
    Return the maximum row number of a dictionary

    Args:
        dict:   A given dictionary

    Returns:
        Maximum row number
    """

    # Check if the input dictionary be empty
    if len(dict.keys()) <= 0:
        vis_msg.print('WARNING in maxMatDictConstantRow: Empty dictionary',
                      type='error')
        return 0

    firstkey = list(dict.keys())[0]
    nrow = len(dict[firstkey])

    for key in dict.keys():
        if nrow > len(dict[key]):
            nrow = len(dict[key])

    return nrow


def filterDictByValue(dict, key, value=0, flag='=='):
    """
    Filter a dictionary by specified key value

    Args:
        dict:   Input dictionary
        key:    Key for filtering
        value:  Filtering threshold. Default is 0
        flag:   Filter operator: '>=', '<=', '==', '>', '<', '!='. Default is '=='

    Returns:
        A dictionary of specified index
    """

    # Check if the input dictionary be empty
    if len(dict.keys()) <= 0:
        vis_msg.print('ERROR in filterDictByValue: Empty dictionary', type='error')
        sys.exit()
    if isDictConstantRow(dict) is False:
        vis_msg.print('ERROR in filterDictByValue: Inconstant row number found in input dictionary', type='error')
        sys.exit()

    # Check key
    if (key in dict.keys()) is False:
        vis_msg.print('ERROR in filterDictByValue: Specified key not found in input dictionary', type='error')
        sys.exit()

    idx = []
    if flag == '>=':
        idx = [k for k, v in enumerate(dict[key]) if v >= value]
    if flag == '<=':
        idx = [k for k, v in enumerate(dict[key]) if v <= value]
    if flag == '==':
        idx = [k for k, v in enumerate(dict[key]) if v == value]
    if flag == '>':
        idx = [k for k, v in enumerate(dict[key]) if v > value]
    if flag == '<':
        idx = [k for k, v in enumerate(dict[key]) if v < value]
    if flag == '!=':
        idx = [k for k, v in enumerate(dict[key]) if v != value]

    if len(idx) <= 0:
        vis_msg.print('WARNING in filterDictByValue: No data found', type='warning')
        return {}

    batch = retrieveDictByIndex(dict, idx)

    return batch


def retrieveDictByKey(dict, key_list):
    """
    Retrieve a given dictionary by specified keys

    Args:
        dict:       Input dictionary
        key_list:   List of keys for retrieval

    Returns:
        A dictionary with the specified keys
    """

    # Check if the input dictionary be empty
    if len(dict.keys()) <= 0:
        vis_msg.print('ERROR in retrieveDictByKeys: Empty dictionary', type='error')
        sys.exit()
    if len(key_list) <= 0:
        vis_msg.print('ERROR in retrieveDictByKeys: Empty key list for retrieval', type='error')
        sys.exit()

    batch = {}
    for key in key_list:
        if key in dict.keys():
            batch[key] = dict[key]
        else:
            vis_msg.print('WARNING in retrieveDictByKeys: ' + key + ' Not found in the input dictionary',
                          type='warning')

    return batch


def retrieveDictByIndex(dict, index_list):
    """
    Retrieve a dictionary by specified index

    Args:
        dict:       Input dictionary, first row of index 0
        index_list: 1D array of index.

    Returns:
        A dictionary of specified index
    """

    # Check if the input dictionary be empty
    if len(dict.keys()) <= 0:
        vis_msg.print('ERROR in retrieveDictByIndex: Empty dictionary', type='error')
        sys.exit()
    if isDictConstantRow(dict) is False:
        vis_msg.print('ERROR in retrieveDictByIndex: Inconstant row number found in input dictionary',
                      type='error')
        sys.exit()

    # Check if the index be empty
    if np.ndim(index_list) < 1:
        vis_msg.print('ERROR in retrieveDictByIndex: 1D index array expected', type='error')
        sys.exit()
    if len(index_list) <= 0:
        vis_msg.print('ERROR in retrieveDictByIndex: Empty index array', type='error')
        sys.exit()

    maxnrow = len(dict[list(dict.keys())[0]])
    if np.max(index_list) >= maxnrow:
        vis_msg.print('ERROR in retrieveDictByIndex: Index list out of bound', type='error')
        sys.exit()

    # Extract all keys
    batch = {}
    for key in dict.keys():
        data_batch = [dict[key][int(i)] for i in index_list]
        data_batch = np.asarray(data_batch)
        batch[key] = data_batch

    return batch


def retrieveDictRandom(dict, batch_size=10, unique=True):
    """
    Retrieve a batch of a given dictionary randomly

    Args:
        dict:       Input dictionary
        batch_size: Size of dictionary batch. Default is 10
        unique:     Unique or not. If so, length of returned dictionary may be shorter than batch_size

    Returns:
        Dictionary batch
    """

    # Check if the input dictionary be empty
    if len(dict.keys()) <= 0:
        vis_msg.print('ERROR in retrieveDictBatchRandom: Empty dictionary', type='error')
        sys.exit()
    if isDictConstantRow(dict) is False:
        vis_msg.print('ERROR in retrieveDictBatchRandom: Inconstant row number found in input dictionary',
                      type='error')
        sys.exit()

    maxnrow = len(dict[list(dict.keys())[0]])

    if batch_size > maxnrow:
        vis_msg.print('WARNING in retrieveDictBatchRandom: Batch size too large', type='warning')
        batch_size = maxnrow

    # Random shuffle
    # idx = np.arange(0, maxnrow)
    # np.random.shuffle(idx)
    # idx = idx[0:batch_size]
    idx = np.random.randint(maxnrow, size=batch_size)
    if unique is True:
        idx = np.unique(idx)

    # Extract all keys
    batch = {}
    for key in dict.keys():
        data_batch = [dict[key][i] for i in idx]
        data_batch = np.asarray(data_batch)
        batch[key] = data_batch

    return batch


def splitDictRandom(dict, fraction=0.9):
    """
    Split a dict randomly

    Args:
        dict:       Input dictionary
        fraction:   Approximate fraction of the rows between 0 and 1

    Returns:
        Two new dictionaries
    """

    # Check if the input dictionary be empty
    if len(dict.keys()) <= 0:
        vis_msg.print('ERROR in splitDictRandom: Empty dictionary', type='error')
        sys.exit()
    if isDictConstantRow(dict) is False:
        vis_msg.print('ERROR in splitDictRandom: Inconstant row number found in input dictionary', type='error')
        sys.exit()

    if fraction <= 0.0 or fraction >= 1.0:
        vis_msg.print('ERROR in splitDictRandom: Fraction be (0.0, 1.0)', type='error')
        sys.exit()

    maxnrow = len(dict[list(dict.keys())[0]])

    nsplit = int(maxnrow * fraction)
    if nsplit <= 0:
        nsplit = 1
    if nsplit >= maxnrow:
        nsplit = maxnrow-1

    # Random shuffle
    idx = np.arange(0, maxnrow)
    np.random.shuffle(idx)
    idx_1 = idx[0:nsplit]
    idx_2 = idx[nsplit: maxnrow]

    # Extract all keys
    batch_1 = {}
    batch_2 = {}
    for key in dict.keys():
        data_batch = [dict[key][i] for i in idx_1]
        batch_1[key] = np.asarray(data_batch)
        data_batch = [dict[key][i] for i in idx_2]
        batch_2[key] = np.asarray(data_batch)

    return batch_1, batch_2


def truncateDict(dict, length=10):
    """
    Truncate a dictionary to a given length, and maximum truncation for the given length <= 0

    Args:
        dict:   Input dictionary
        length: Truncation length. Default is 10
                Maximum truncation if the given length <= 0

    Returns:
        Truncated dictionary
    """

    # Check if the input dictionary be empty
    if len(dict.keys()) <= 0:
        vis_msg.print('ERROR in truncateDict: Empty dictionary', type='error')
        sys.exit()

    firstkey = list(dict.keys())[0]
    maxlen = np.shape(dict[firstkey])[0]
    for key in dict.keys():
        len_key = np.shape(dict[key])[0]
        if maxlen > len_key:
            maxlen = len_key

    if length<=0 or length>maxlen:
        vis_msg.print('WARNING in truncateDict: Maximum truncation performed', type='warning')
        length = maxlen

    idx = np.linspace(0, length-1, num=length, dtype=int)
    batch = {}
    for key in dict.keys():
        data_batch = [dict[key][i] for i in idx]
        data_batch = np.asarray(data_batch)
        batch[key] = data_batch

    return batch


def isMatDict(dict):
    """
    Check if all dictionary values are of type numpy.ndarray

    Args:
        dict:       The given dictionary

    Returns:
        True or false
    """

    # Check if the input dictionary be empty
    if len(dict.keys()) <= 0:
        vis_msg.print('ERROR in isMatDict: Empty input dictionary', type='error')
        sys.exit()

    for key in dict.keys():
        if type(dict[key]) != np.ndarray:
            return False

    return True


def extractMatDict(dict):
    """
    Extract the dictionary values of numpy.ndarray as a separate dictionary

    Args:
        dict:   a dictionary

    Returns:
        a dictionary with all values of type numpy.ndarray
    """

    if len(dict.keys()) <= 0:
        vis_msg.print('ERROR in extractNumDict: Empty input dictionary', type='error')
        sys.exit()

    numdict = {}
    for key in dict.keys():
        if type(dict[key]) == np.ndarray:
            numdict[key] = dict[key]

    return numdict


def mergeMatDict(dict1, dict2):
    """
    Merge two matrix dictionaries by their keys

    Args:
        dict1:  first matrix dictionary
        dict2: second matrix dictionary

    Returns:
        A new matrix dictionary
    """

    if (isMatDict(dict1) is False) or (isMatDict(dict2) is False):
        vis_msg.print('ERROR in mergeMatDict: Matrix dictionary expected', type='error')
        sys.exit()

    batch = dict1.copy()
    for key in dict2.keys():
        if (key in dict1.keys()):
            if np.shape(batch[key])[1] == np.shape(dict2[key])[1]:
                batch[key] = np.concatenate((batch[key], dict2[key]))
            else:
                vis_msg.print('WARNING: Inconstant matrix width in two dictionaries', type='warning')
        else:
            batch[key] = dict2[key]

    return batch


def exportMatDict(dict, key_list=None):
    """
    Export a matrix dictionary as a numpy matrix

    Args:
        dict:       input matrix dictionary
        key_list:   list of keys for export. Default is None to export all keys

    Returns:
        matrix
    """

    # Check if the input dictionary be empty
    if len(dict.keys()) <= 0:
        vis_msg.print('ERROR in exportMatDict: Empty dictionary', type='error')
        sys.exit()
    if isMatDict(dict) is False:
        vis_msg.print('ERROR in exportMatDict: Matrix dictionary expected', type='error')
        sys.exit()

    if key_list is None:
        vis_msg.print('WARNING in exportMatDict: Export all keys', type='warning')
        key_list = dict.keys()
    if len(key_list) <= 0:
        vis_msg.print('ERROR in exportMatDict: Empty key list for export', type='error')
        sys.exit()


    mat = []
    for key in key_list:
        if key in dict.keys():
            if len(mat) == 0:
                mat = dict[key]
            else:
                if np.shape(mat)[0] == np.shape(dict[key])[0]:
                    mat = np.concatenate((mat, dict[key]), axis=1)
                else:
                    vis_msg.print('ERROR in exportMatDict: ' + key + ' of inconstant row number', type='error')
                    sys.exit()

    return mat


def extendMatDict(dict, length=100):
    """
    Extend a matrix dictionary to a given length

    Args:
        dict:   input matrix dictionary
        length: extended length. Default is 100

    Returns:
        Extended dictionary
    """

    if isMatDict(dict) is False:
        vis_msg.print('ERROR in extendMatDict: Matrix dictionary expected', type='error')
        sys.exit()

    maxlen = maxDictConstantRow(dict)

    if length <= maxlen:
        vis_msg.print('WARNING in extendDict: No extension performed', type='warning')
        length = maxlen

    batch = dict.copy()
    while maxDictConstantRow(batch) < length:
        lendiff = length - maxDictConstantRow(batch)
        if lendiff > maxlen:
            batch0 = dict.copy()
        else:
            batch0 = retrieveDictRandom(dict, lendiff)
        batch = mergeMatDict(batch, batch0)

    return batch


class matdict:
    # Pack all functions as a class
    #
    isDictConstantRow = isDictConstantRow
    maxDictConstantRow = maxDictConstantRow
    #
    filterDictByValue = filterDictByValue
    #
    retrieveDictByIndex = retrieveDictByIndex
    retrieveDictByKey = retrieveDictByKey
    retrieveDictRandom = retrieveDictRandom
    #
    splitDictRandom = splitDictRandom
    truncateDict = truncateDict
    #
    isMatDict = isMatDict
    extractMatDict = extractMatDict
    mergeMatDict = mergeMatDict
    exportMatDict = exportMatDict
    extendMatDict = extendMatDict