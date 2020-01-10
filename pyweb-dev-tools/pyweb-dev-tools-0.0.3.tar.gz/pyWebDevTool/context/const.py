# -*- coding: utf-8 -*-

from pyWebDevTool.context.globalContext import Context
from pyWebDevTool.util import argumentUtil, configUtil
from pyWebDevTool.util import fileUtil

DEV_WEB_ROOT_PATH = configUtil.get_config_val(configUtil.BaseConfigEnum.webpack_root_path)
DEV_PLUGIN_RELATIVE_PATH = configUtil.get_config_val(configUtil.BaseConfigEnum.webpack_plugin_path)
DEV_WEB_ROOT_ABS_PATH = fileUtil.getRootPath() + DEV_WEB_ROOT_PATH
DEV_STORE_PLUGIN_PATH = DEV_WEB_ROOT_ABS_PATH + DEV_PLUGIN_RELATIVE_PATH
DEV_MODULE_PATH = (DEV_WEB_ROOT_PATH[1:len(DEV_WEB_ROOT_PATH)] + DEV_PLUGIN_RELATIVE_PATH).replace("/", ".")

PLUGIN_STORE = "pluginStore"
PLUGIN_STORE_PATH = fileUtil.getRootPath() + "/" + PLUGIN_STORE
PLUGIN_STORE_JSON_PATH = PLUGIN_STORE_PATH + "/plugin-store.json"

BROWSER_URL = [
    "https://blog.csdn.net/v2sking",
    "https://gitee.com/luanhaoyu_admin/py-web-dev-tools"
]


def getINDEX_RELATIVE_PATH():
    if argumentUtil.is_exe():
        return fileUtil.getRootPath() + "/resources/static/index.html"
    else:
        # return fileUtil.getParentPath(__file__) + "/resources/static/pyweb-dev-tools.html"
        return Context().webpack_server.index_url
