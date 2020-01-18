from webob import Request

class Middleware:

    # Defaults
    code_check_point = 100 
    service_name = None
    log_level = "info"
    encoding = 'utf-8'

    def __init__(self, app, log_level="info", service_name=""):
        self.wrap_app = self.app = app 
        self.set_code_check_point(log_level.lower())
        self.service_name = service_name.lower()
        self.log_level = log_level.lower()
        self.encoding = 'utf-8'

    def __call__(self,environ,start_response):
        request = Request(environ)
        def custom_start_response(status, headers, exc_info=None):
            response = self.app(environ, start_response)
            self.print_log(request,response,status)
            return response
        return self.wrap_app(environ, custom_start_response)

    def set_code_check_point(self,log_level):
        if log_level == "error":
            self.code_check_point = 400 

    def print_log(self,request,response,status):
        code = int(status.split(" ")[0])
        if(code >= self.code_check_point):
            message = ""
            if response != None and len(response) > 0:
                message = response[0].decode("utf-8").replace('"', '\\"') 
            print('{"level":"'+self.log_level+'","service":"'+self.service_name+'","message":"'+message+'","uri":"'+request.path_qs+'","responseCode":'+str(code)+',"requestId":"'+request.headers.get("request-id","")+'"}')
