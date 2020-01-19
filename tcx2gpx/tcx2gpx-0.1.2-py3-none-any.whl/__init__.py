"""
Initialise the module.
"""
import logging
import sys

LOG_FORMATTER = logging.Formatter('%(asctime)s [%(levelname)s][%(name)s] %(message)s',
                                  datefmt="%Y-%m-%d %H:%MS")
LOG_ERR_FORMATTER = logging.Formatter(
    '%(asctime)s [%(levelname)s][%(name)s][%(filename)s:%(lineno)d] %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S")
LOGGER_NAME = 'tcx2gpx'

STD_OUT_STREAMHANDLER = logging.StreamHandler(sys.stdout)
STD_OUT_STREAMHANDLER.setLevel(logging.DEBUG)
STD_OUT_STREAMHANDLER.setFormatter(LOG_FORMATTER)

STD_ERR_STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STD_ERR_STREAM_HANDLER.setLevel(logging.ERROR)
STD_ERR_STREAM_HANDLER.setFormatter(LOG_ERR_FORMATTER)
