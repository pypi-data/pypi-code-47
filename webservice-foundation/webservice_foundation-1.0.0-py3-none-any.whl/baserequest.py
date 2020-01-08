import json

from tornado.web import RequestHandler
from tornado.httputil import parse_body_arguments
from .bodydata import BodyData, ConcatBodyData
from .originaljsonencoder import OriginalJsonEncoder
from .caseInsensitivedict import CaseInsensitiveDict


class BaseRequestHandler(RequestHandler):

    BODY = 'body'
    BODY_ARGS = 'body_args'
    QUERY_ARGS = 'query_args'

    def initialize(self, **kwargs):
        x_auth_token = 'x-auth-token'
        self.x_auth_token = {}
        self.request_header: CaseInsensitiveDict = CaseInsensitiveDict(
            self.request.headers)
        self.remote_ip = self.request_header.get(
            'x-real-ip', self.request.remote_ip)
        if x_auth_token in self.request_header:
            self.request_header[x_auth_token] = json.loads(
                self.request_header[x_auth_token])
            self.x_auth_token = self.request_header[x_auth_token]
        content_type: str = self.request_header.get('Content-Type', '')

        def getArgs(user_args: dict):
            data = {}
            if user_args:
                for key, value in user_args.items():
                    if key not in data:
                        data[key] = []

                    if isinstance(value, list):
                        for v in value:
                            if isinstance(v, bytes):
                                data[key].append(v.decode('utf-8'))
                            else:
                                data[key].append(v)
                    else:
                        data[key].append(value)
            return data
            # return BodyData(data)

        _dict = {
            self.BODY: BodyData({}),
            self.BODY_ARGS: BodyData({}),
            self.QUERY_ARGS: BodyData({})
        }
        if content_type.startswith('application/json'):
            if self.request.body:
                _dict[self.BODY].update(
                    BodyData(json.loads(self.request.body)))

        body_argument = getArgs(self.request.body_arguments)
        if body_argument:
            _dict[self.BODY_ARGS].update(BodyData(body_argument))

        query_argument = getArgs(self.request.query_arguments)
        if query_argument:
            _dict[self.QUERY_ARGS].update(BodyData(query_argument))
        self.bodydata = ConcatBodyData(_dict)

    def json_write(self, data):
        self.write(json.dumps(data, ensure_ascii=False,
                              cls=OriginalJsonEncoder))
