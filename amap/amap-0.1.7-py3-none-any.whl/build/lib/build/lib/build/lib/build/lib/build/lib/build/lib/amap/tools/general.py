"""
general
===============

General tools, used across amap

"""

import os
import argparse
import logging
import numpy as np
import pandas as pd

from natsort import natsorted

from amap.tools import system


def initialise_df(*column_names):
    """
    Initialise a pandasdataframe with n column names
    :param str column_names: N column names
    :return: Empty pandas dataframe with specified column names
    """
    return pd.DataFrame(columns=column_names)


def delete_temp(directory, paths, prefix="tmp__"):
    """
    Removes all temp files (properties of an object starting with "tmp__")
    :param directory: Directory to delete tmp files from
    :param paths: Paths object with temp paths.
    :param prefix: String that temporary files (to be deleted) begin with.
    """
    for path_name, path in paths.__dict__.items():
        if path_name.startswith(prefix):
            if system.check_path_in_dir(path, directory):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    logging.debug(
                        f"File: {path} not found, not deleting. "
                        f"Proceeding anyway."
                    )


def scale_to_16_bits(img):
    """
    Normalise the input image to the full 0-2^16 bit depth.

    :param np.array img: The input image
    :return: The normalised image
    :rtype: np.array
    """
    normalised = img / img.max()
    return normalised * (2 ** 16 - 1)


def scale_and_convert_to_16_bits(img):
    """
    Normalise the input image to the full 0-2^16 bit depth, and return as
    type: "np.uint16".

    :param np.array img: The input image
    :return: The normalised, 16 bit image
    :rtype: np.array
    """
    img = scale_to_16_bits(img)
    return img.astype(np.uint16, copy=False)


def check_positive_float(value, none_allowed=True):
    """
    Used in argparse to enforce positive floats
    FromL https://stackoverflow.com/questions/14117415
    :param value: Input value
    :param none_allowed: If false, throw an error for None values
    :return: Input value, if it's positive
    """
    ivalue = value
    if ivalue is not None:
        ivalue = float(ivalue)
        if ivalue < 0:
            raise argparse.ArgumentTypeError(
                "%s is an invalid positive value" % value
            )
    else:
        if not none_allowed:
            raise argparse.ArgumentTypeError("%s is an invalid value." % value)

    return ivalue


def check_positive_int(value, none_allowed=True):
    """
    Used in argparse to enforce positive ints
    FromL https://stackoverflow.com/questions/14117415
    :param value: Input value
    :param none_allowed: If false, throw an error for None values
    :return: Input value, if it's positive
    """
    ivalue = value
    if ivalue is not None:
        ivalue = int(ivalue)
        if ivalue < 0:
            raise argparse.ArgumentTypeError(
                "%s is an invalid positive value" % value
            )
    else:
        if not none_allowed:
            raise argparse.ArgumentTypeError("%s is an invalid value." % value)

    return ivalue


def remove_empty_string_list(str_list):
    """
    Removes any empty strings from a list of strings
    :param str_list: List of strings
    :return: List of strings without the empty strings
    """
    return list(filter(None, str_list))


def get_text_lines(
    file,
    return_lines=None,
    rstrip=True,
    sort=False,
    remove_empty_lines=True,
    encoding=None,
):
    """
    Return only the nth line of a text file
    :param file: Any text file
    :param return_lines: Which specific line/lines to read
    :param rstrip: Remove trailing characters
    :param sort: If true, naturally sort the data
    :param remove_empty_lines: If True, ignore empty lines
    :param encoding: What encoding the text file has.
    Default: None (platform dependent)
    :return: The nth line
    """
    with open(file, encoding=encoding) as f:
        lines = f.readlines()
    if rstrip:
        lines = [line.strip() for line in lines]
    if remove_empty_lines:
        lines = remove_empty_string_list(lines)
    if sort:
        lines = natsorted(lines)
    if return_lines is not None:
        lines = lines[return_lines]
    return lines


def suppress_specific_logs(logger, message):
    logger = logging.getLogger(logger)

    class NoParsingFilter(logging.Filter):
        def filter(self, record):
            return not record.getMessage().startswith(message)

    logger.addFilter(NoParsingFilter())
