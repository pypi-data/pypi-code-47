# -*- coding: utf-8 -*-


class PrivateRouteContext:
    def __init__(self):
        self.routes = {}

    def route(self, route_str):
        def decorator(f):
            self.routes[route_str] = f
            return f

        return decorator

    def serve(self, path, params=None):
        view_function = self.routes.get(path)
        if view_function:
            return view_function(params)
        else:
            raise ValueError('Route "{}"" has not been registered'.format(path))


_private_rc = PrivateRouteContext()
