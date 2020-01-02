import json
from functools import update_wrapper

from tornado.web import (
    RequestHandler,
    Application
)

class ServiceNotFoundError(Exception):
    def __str__(self):
        return repr("The request service was not found")

class ServiceArgumentError(Exception):
    def __str__(self):
        return repr("Service is missing one or more arguments")

class Servicemethod(object):
    __slots__ = ("method", "arg_list")

    def __init__(self, method, arg_list):
        self.method = method
        self.arg_list = arg_list

class WSApplication(Application):
    """A webservice application. 

    This class is derivced from tornado's ``Application`` class. 
    Each new webservice is added to this class's ``endpoint`` class variable. 
    When initialized, ``endpoints`` becomes this application's handlers list. 
    """
    endpoints = []

    def __init__(self, **settings):
        super(WSApplication, self).__init__(self.endpoints, **settings)

class BaseWebserviceHandler(RequestHandler):
    """A webservice handler. 
    
    This class is derived from tornado's ``RequestHandler`` class. 
    New service methods are added to this class's ``servicemethods`` class 
    variable. 
    """
    servicemethods = {}

    @classmethod
    def register_servicemethod(
        cls, 
        cls_name, 
        httpmethod, 
        methodname, 
        servicemethod
    ):
        # the class name must be added here because the class is still 
        # being made when servicemethod is called meaning that the 
        # webservice decorator has not finished
        if cls_name not in cls.servicemethods:
            cls.servicemethods[cls_name] = {}
        if httpmethod not in cls.servicemethods[cls_name]:
            cls.servicemethods[cls_name][httpmethod] = {}
        cls.servicemethods[cls_name][httpmethod][methodname] = servicemethod

    def get_servicemethod(self, methodname: str) -> "Servicemethod":
        """Gets service method ``methodname`` from this request handler"""
        svc_pool = self.servicemethods.get(self.__class__.__name__, None)
        if svc_pool is not None:
            method_pool = svc_pool.get(self.request.method, None)
            if method_pool is not None:
                servicemethod = method_pool.get(methodname, None)
                if servicemethod is not None:
                    return servicemethod
        raise ServiceNotFoundError

    def prepare(self):
        """Parses query arguments for GET request, body arguments for other"""
        if self.request.method == "GET":
            self.args = self.read_query()
        else:
            self.args = self.read_body()

    def read_query(self):
        query = self.request.query
        args = {}
        if not query:
            return args
        for arg in query.split("&"):
            k, v = arg.split("=")
            v = self.decode_argument(v)
            args[k] = v
        return args

    def read_body(self):
        """Reads request body and parses arguments."""
        body = self.request.body
        if not body:
            return {}
        return self.load(body)

    def validate_args(self, servicemethod, args):
        """Checks to ensure that all arguments are available. 

        Override to customize argument validation and error handling. 
        """
        for arg in servicemethod.arg_list:
            if arg not in args:
                raise ServiceArgumentError

    def load(self, request):
        """Controls how requests are loaded before they are fulfilled. 

        By default, responses are converted to JSON with json.loads.
        Override to customize supported input type (i.e. xml/yaml/etc.)
        """
        return json.loads(request)
    
    def dump(self, response):
        """Controls how responses are dumped before they are sent. 

        By default, responses are converted to JSON with json.dumps. 
        """
        self.set_header("Content-Type", "application/json")
        return json.dumps(response)

    def write(self, response):
        """dumps and sends the response to the client. 

        By default, responses are converted to JSON. 
        To change this behavior, override the dump method. 
        """
        super(BaseWebserviceHandler, self).write(self.dump(response))
        self.finished = True

    def on_finish(self):
        self.finished = True

class WebserviceHandler(BaseWebserviceHandler):
    __doc__ = BaseWebserviceHandler.__doc__

    async def complete_request(self, path):
        """Finds the requested service and conducts response preperation."""
        try:
            servicemethod = self.get_servicemethod(path)
            self.validate_args(servicemethod, self.args)
            response = await servicemethod.method(self, **self.args)
            if not getattr(self, "finished", False):
                self.write(response)
        except ServiceNotFoundError:
            self.send_error(404)
        except ServiceArgumentError:
            self.send_error(400)

class SyncWebserviceHandler(BaseWebserviceHandler):
    __doc__ = BaseWebserviceHandler.__doc__

    def complete_request(self, path):
        """Finds the requested service and conducts response preperation."""
        try:
            servicemethod = self.get_servicemethod(path)
            self.validate_args(servicemethod, self.args)
            response = servicemethod.method(self, **self.args)
            if not getattr(self, "finished", False):
                self.write(response)
        except ServiceNotFoundError:
            self.send_error(404)
        except ServiceArgumentError:
            self.send_error(400)

def webservice(cls):
    """This decorator includes a class in the ``WSApplication`` as a webservice.

    The webservice's path is derived from the class name. 
    - for example, MyWebService becomes /my-web-service. 
    """
    servicename = _classname_to_path(cls.__name__)
    path = f"/{servicename}/(.+?)"
    httpmethods = cls.SUPPORTED_METHODS
    if issubclass(cls, SyncWebserviceHandler):
        def handle_method(self, path):
            self.complete_request(path)
    else:
        async def handle_method(self, path):
            await self.complete_request(path)
    for httpmethod in httpmethods:
        httpmethod = httpmethod.lower()
        if(getattr(cls, httpmethod, RequestHandler._unimplemented_method) 
                is RequestHandler._unimplemented_method):
            setattr(cls, httpmethod, handle_method)
    WSApplication.endpoints.append((path, cls))
    return cls

def servicemethod(httpmethod="POST"):
    """This decorator creates a service method from a ``BaseWebserviceHandler`` method. 

    The method's path is derived from its name. 
    - for example, square_root becomes /{servicename}/square-root. 
    """
    if not httpmethod.isupper():
        httpmethod = httpmethod.upper()
    def decorating_function(f):
        # get the class name from the function definition
        cls_name = f.__qualname__.split(".")[0]
        methodname = f.__name__.replace("_", "-")
        c = f.__code__
        # NOTE: This assumes that function arguments are first in co_varname 
        # and that "self" is the first argument. Self is skipped because it 
        # does not need to be validated
        # TODO: Add support for optional arguments
        arg_list = c.co_varnames[1:c.co_argcount]
        BaseWebserviceHandler.register_servicemethod(
            cls_name, 
            httpmethod, 
            methodname, 
            Servicemethod(f, arg_list)
        )
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return update_wrapper(wrapper, f)
    return decorating_function

def _classname_to_path(servicename):
    path = []
    for i, c in enumerate(servicename):
        if c.isupper():
            if i > 0:
                path.append("-")
            path.append(c.lower())
        else:
            path.append(c)
    return "".join(path)
