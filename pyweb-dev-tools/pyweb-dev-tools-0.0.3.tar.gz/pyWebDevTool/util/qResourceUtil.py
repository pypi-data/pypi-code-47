# -*- coding: utf-8 -*-

from PyQt5.QtGui import QIcon

from pyWebDevTool.util import qFileUtil


def get_qss(file_name):
    return qFileUtil.read_str_file(":/qss/resources/style/" + file_name)


def get_ico(ico_name):
    return QIcon(":/qss/resources/ico/" + ico_name)
