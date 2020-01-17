from Spitzer.chache import chache
from Spitzer.config import config

from distutils.dir_util import copy_tree
import os


def quit(error=False): #runs on exit, for doing cleanup   
    if error:
        try:
            os.mkdir(os.getcwd() + '/debug')
        except FileExistsError:
            pass
        copy_tree(chache.get_path(), os.getcwd() + '/debug')
    chache.clear()