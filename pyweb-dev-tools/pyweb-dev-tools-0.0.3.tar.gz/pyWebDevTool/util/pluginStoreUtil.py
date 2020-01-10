# -*- coding: utf-8 -*-
import json

from pyWebDevTool.context import const
from pyWebDevTool.context.const import PLUGIN_STORE, PLUGIN_STORE_PATH, PLUGIN_STORE_JSON_PATH
from pyWebDevTool.context.globalContext import Context
from pyWebDevTool.util import jsonUtil, argumentUtil, fileUtil
from pyWebDevTool.util.loggerFactory import Logger

logger = Logger()


def read_json():
    return jsonUtil.read_file(PLUGIN_STORE_JSON_PATH)


def read_class_json():
    """按分类获取"""
    packages = jsonUtil.read_file(PLUGIN_STORE_JSON_PATH)
    classes = []
    json = {}
    for p in packages:
        if not classes.__contains__(p['class']):
            json[p['class']] = []
            classes.append(p['class'])

    for c in classes:
        for p in packages:
            if c == p['class']:
                json[c].append(p)
    return json


def write_json(jsons):
    # 保存
    with open(PLUGIN_STORE_JSON_PATH, 'w', encoding="utf-8") as f:
        f.write(json.dumps(jsons, ensure_ascii=False, indent=2))


def get_plugin_path(package_info):
    p_path = "{}/{}/{}".format(PLUGIN_STORE_PATH, package_info["groupId"].replace(".", "/"), package_info["artifactId"])
    return p_path


def get_plugin_index_path(package_info):
    if argumentUtil.is_dev():
        return Context().webpack_server.index_url + "#" + package_info['indexPath']
    else:
        return get_plugin_path(package_info) + "/web/index.html#" + package_info['indexPath']
        # return get_plugin_path(package_info) + "/web/index.html"


def get_dev_plugin_module(package_info):
    return "{}.{}.{}.{}".format(const.DEV_MODULE_PATH, package_info['groupId'], package_info['artifactId'],
                                package_info['router'].replace(".py", ""))


def get_prod_plugin_module(package_info):
    return "{}.{}.{}.{}".format(PLUGIN_STORE, package_info["groupId"], package_info["artifactId"],
                                package_info["router"].replace(".py", ""))


def get_plugin_module(package_info):
    if argumentUtil.is_dev():
        return get_dev_plugin_module(package_info)
    else:
        return get_prod_plugin_module(package_info)


def del_plugin(group_id, artifact_id):
    jsons = read_json()
    index = 0
    for p in jsons:
        if p["groupId"] == group_id and p["artifactId"] == artifact_id:
            del jsons[index]
            # 删除插件包文件
            path = get_plugin_path(p)
            logger.info("删除插件包文件:" + path)
            fileUtil.delDir(path)
            break
        index = index + 1
    write_json(jsons)
