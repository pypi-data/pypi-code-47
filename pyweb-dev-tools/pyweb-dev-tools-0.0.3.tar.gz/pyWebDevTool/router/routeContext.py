# -*- coding: utf-8 -*-
import os
import traceback

import pyWebDevTool.context.const
from pyWebDevTool.context import const
from pyWebDevTool.router.private.privateRouteContext import PrivateRouteContext
from pyWebDevTool.util import fileUtil, argumentUtil


class RouteContext:
    def __init__(self):
        self.routes = {}

    def route(self, route_str):
        s = traceback.extract_stack()
        index = 0
        i = 0
        for s1 in s:
            if s1.filename == __file__:
                i = index - 1
                index += 1
                break
            index += 1
        if argumentUtil.is_dev():
            module_name = s[i].filename.replace(fileUtil.getRootPath(), "") \
                .replace(os.path.sep, "/") \
                .replace(const.DEV_STORE_PLUGIN_PATH, "") \
                .replace(".py", "")
        else:
            module_name = s[i].filename.replace(fileUtil.getRootPath(), "") \
                .replace(os.path.sep, "/") \
                .replace("/" + pyWebDevTool.context.const.PLUGIN_STORE, "") \
                .replace(".py", "")
        route_str = module_name + route_str

        def decorator(f):
            self.routes[route_str] = f
            return f

        return decorator

    def serve(self, path, params=None):
        if argumentUtil.is_dev():
            path = const.DEV_WEB_ROOT_PATH + const.DEV_PLUGIN_RELATIVE_PATH + path

        view_function = self.routes.get(path)
        if view_function:
            return view_function(params)
        else:
            raise ValueError('Route "{}"" has not been registered'.format(path))


rc = RouteContext()
