# -*- coding: utf-8 -*-
import os

from pyWebDevTool.context import const
from pyWebDevTool.util import fileUtil, zipUtil, packageInfoUtil, argumentUtil

PLUGIN_DIST_PATH = fileUtil.getRootPath() + "/pluginDist/"
PLUGIN_BUILD_PATH = fileUtil.getRootPath() + "/pluginBuild/"


def ignore(src, names):
    return src + "/web"


def build():
    os.chdir(fileUtil.getRootPath())
    if not argumentUtil.has_sys_arg("-bWeb=n"):
        print("cd vuedev")
        os.chdir("vuedev")
        print("npm run build")
        os.system("npm run build")
        print("cd ..")
        os.chdir("..")
    fileUtil.delDir(PLUGIN_DIST_PATH, is_del_root=False)
    fileUtil.mkdir(PLUGIN_DIST_PATH)
    fileUtil.delDir(PLUGIN_BUILD_PATH, is_del_root=False)
    fileUtil.mkdir(PLUGIN_BUILD_PATH)
    plugin_root_path = const.DEV_STORE_PLUGIN_PATH
    plugin_info = packageInfoUtil.get_package_infos(plugin_root_path)
    for p in plugin_info:
        p_folder_path = "/{}/{}".format(p['groupId'].replace(".", "/"), p['artifactId'])

        fileUtil.copyFolder(plugin_root_path + p_folder_path, PLUGIN_BUILD_PATH + p_folder_path, ignore=ignore)
        fileUtil.copyFolder(const.DEV_WEB_ROOT_ABS_PATH + os.path.sep + "dist",
                            PLUGIN_BUILD_PATH + p_folder_path + "/web")
        os.chdir(PLUGIN_DIST_PATH)
        zipUtil.zip(p['artifactId'] + "-" + p['version'], PLUGIN_BUILD_PATH)
    fileUtil.delDir(PLUGIN_BUILD_PATH)
    return plugin_info
