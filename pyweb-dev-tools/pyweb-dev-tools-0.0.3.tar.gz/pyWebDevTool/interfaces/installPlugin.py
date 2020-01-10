# -*- coding: utf-8 -*-
import os

import pyWebDevTool.context.const
from pyWebDevTool.util import httpUtil, fileUtil, randomUtil, zipUtil, packageInfoUtil, timeUtil, \
    pluginStoreUtil
from pyWebDevTool.util.loggerFactory import Logger

TEMP_PATH = fileUtil.getRootPath() + "/temp"

logger = Logger()


def install(plugin_path=None, url=None):
    """安装插件包"""
    if plugin_path is None and url is None:
        raise OSError("参数不能为空")
    temp_zip_folder = TEMP_PATH + "/" + randomUtil.random_str()
    temp_zip_path = temp_zip_folder + ".zip"
    # 移动或下载文件
    if url is not None:
        httpUtil.downloadFile(url, temp_zip_path)
    if plugin_path is not None:
        fileUtil.move(plugin_path, temp_zip_path)
    # 解压文件
    zipUtil.unzip_all(temp_zip_path, temp_zip_folder)

    # 获取包信息
    packageInfo = packageInfoUtil.get_package_info(temp_zip_folder)
    if packageInfo is not None:
        # 获取仓库信息
        pluginJson = pluginStoreUtil.read_json()
        if len(pluginJson) == 0:
            __add_plugin(packageInfo, pluginJson, temp_zip_folder)
        else:
            # 准备往插件仓库移动
            # 读取仓库配置文件配置文件校验是否存在
            update_flag = False
            for p in pluginJson:
                if packageInfo['groupId'] == p["groupId"] and packageInfo['artifactId'] == p["artifactId"]:
                    update_flag = True
                    __update_plugin(p, packageInfo, pluginJson, temp_zip_folder)
                    break
            if not update_flag:
                __add_plugin(packageInfo, pluginJson, temp_zip_folder)
        return packageInfo
    fileUtil.delDir(TEMP_PATH)
    return {}



def __update_plugin(p, packageInfo, pluginJson, temp_zip_folder):
    logger.info(
        "开始安装插件：{}.{} 已存在。原版本号：{},新版本号：{}".format(packageInfo["groupId"], packageInfo["artifactId"],
                                                  p["version"], packageInfo["version"]))
    # 更新仓库信息
    p['version'] = packageInfo["version"]
    # 复制插件到包目录
    fileUtil.copyFolder(temp_zip_folder, pyWebDevTool.context.const.PLUGIN_STORE_PATH, override=True)
    p['installTime'] = timeUtil.time2str()
    pluginStoreUtil.write_json(pluginJson)


def __add_plugin(packageInfo, pluginJson, temp_zip_folder):
    logger.info(
        "开始安装插件：{}.{}。版本号：{}".format(packageInfo["groupId"], packageInfo["artifactId"],
                                     packageInfo["version"]))
    p = packageInfo
    # 复制插件到包目录
    fileUtil.copyFolder(temp_zip_folder, pyWebDevTool.context.const.PLUGIN_STORE_PATH, override=True)
    p['installTime'] = timeUtil.time2str()
    pluginJson.append(p)
    pluginStoreUtil.write_json(pluginJson)
