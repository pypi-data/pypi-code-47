# -*- coding: utf-8 -*-
from pyWebDevTool.context.globalContext import Context
from pyWebDevTool.router.private.privateRouteContext import _private_rc
from pyWebDevTool.util import pluginStoreUtil, listUtil, dictUtil
from pyWebDevTool.util.loggerFactory import Logger

logger = Logger()


class PluginContext:

    def open_plugin_install_dialog(self, params):
        Context().mainWindowImpl.open_plugin_install_dialog()

    def del_plugin(self, params):
        groupId = params['groupId']
        artifactId = params['artifactId']
        pluginStoreUtil.del_plugin(groupId, artifactId)


pluginContext = PluginContext()


@_private_rc.route("/plugin/list")
def plugin_list(params):
    """获取插件列表"""
    logger.info("--------------------获取插件列表---------------------，参数params：{}".format(params))
    pageSize = params['pageSize']  # 每页大小
    pageNumber = params['pageNumber']  # 页号
    searchCode = params['searchCode']  # 页号
    lists = pluginStoreUtil.read_json()
    n_list = []
    if searchCode != '':
        for l in lists:
            if dictUtil.like_key(l, 'groupId', searchCode) \
                    or dictUtil.like_key(l, 'artifactId', searchCode) \
                    or dictUtil.like_key(l, 'version', searchCode) \
                    or dictUtil.like_key(l, 'name', searchCode) \
                    or dictUtil.like_key(l, 'class', searchCode) \
                    or dictUtil.like_key(l, 'description', searchCode):
                n_list.append(l)
    else:
        n_list = lists
    return listUtil.paging(n_list, page_size=pageSize, page_number=pageNumber)


@_private_rc.route("/plugin/del")
def plugin_del(params):
    """删除插件列表"""
    logger.info("--------------------删除插件列表---------------------，参数params：{}".format(params))
    Context().mainThreadDelegate.move_to_ui_thread(obj=pluginContext, function="del_plugin",
                                                   params=params)
    return 0


@_private_rc.route("/plugin/open_add")
def open_add(params):
    """打开新增插件窗口"""
    logger.info("--------------------打开新增插件窗口---------------------，参数params：{}".format(params))
    Context().mainThreadDelegate.move_to_ui_thread(obj=pluginContext, function="open_plugin_install_dialog",
                                                   params=params)
    return 0
