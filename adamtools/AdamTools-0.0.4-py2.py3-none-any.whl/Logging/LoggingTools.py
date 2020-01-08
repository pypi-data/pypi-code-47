"""
Created by adam on 11/24/16
"""
__author__ = 'adam'

from datetime import datetime
from logbook import Logger
import os


class LogWriter(object):
    """
    Parent class for loggers which write to a textfile
    """

    def __init__(self):
        self.initialize_logger()

    def initialize_logger(self):
        try:
            if self.logger is not None:
                pass
        except:
            self.logger = Logger()
            # self.logger = FileHandler(self.CLIENT_SEND_LOG_FILE)
            # self.logger.push_application() #Pushes handler onto stack of log handlers

    def set_log_file(self, file_to_write):
        """
        Sets the file to which log entries will be written
        Args:
            file_to_write: Full path to log file
        """
        self.logfile = file_to_write

    def write(self, stuff):
        with open(self.logfile, 'a') as f:
            f.write(stuff)
            f.close()
