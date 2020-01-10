# -*- coding: utf-8 -*-
import json
import os
import re

from pyWebDevTool.context import const
from pyWebDevTool.util import fileUtil, argumentUtil
from pyWebDevTool.util.jsonUtil import replace_json_comment


def get_package_info(root_dir):
    plugin_paths = fileUtil.listFile(root_dir)
    file_json = None
    for p in plugin_paths:
        if os.path.basename(p).endswith('package-info.js'):
            file_json = read_package_info_js(p)
            break
    return file_json


def get_package_infos(root_dir):
    plugin_infos = []
    plugin_paths = fileUtil.listFile(root_dir)
    for p in plugin_paths:
        if os.path.basename(p).endswith('package-info.js'):
            file_json = read_package_info_js(p)
            plugin_infos.append(file_json)
    return plugin_infos


def list_package_infos():
    if argumentUtil.is_dev():
        return get_package_infos(const.DEV_STORE_PLUGIN_PATH)
    else:
        return get_package_infos(const.PLUGIN_STORE_PATH)


def read_package_info_js(p):
    with open(p, "r", encoding="utf-8") as f:
        content = replace_json_comment(f.read())
        replace = content.replace("export", "").replace("default", "")
    return json.loads(replace)


def get_package_info_id(package):
    return "{}_{}".format(package['groupId'], package['artifactId'])
