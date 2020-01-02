import enum
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List

import requests
from requests import Session

_DEFAULT_NUM_OF_WORKERS = 1
_DEFAULT_TIMEOUT_SECONDS = 15


class HTTPMethod(enum.Enum):
    GET = 1
    POST = 2
    PUT = 3
    PATCH = 4
    DELETE = 5


class RequestOptions(object):
    def __init__(self, timeout_seconds: int = _DEFAULT_TIMEOUT_SECONDS, workers_count: int = _DEFAULT_NUM_OF_WORKERS):
        self.workers_count = workers_count
        self.timeout_seconds = timeout_seconds


class Requester(object):
    
    @staticmethod
    def _make_request(request_obj: requests.Request, id_: int, timeout=int) -> (requests.Response, int):
        pr = request_obj.prepare()
        response = Session().send(pr, timeout=timeout)
        return response, id_
    
    @staticmethod
    def do_requests(request_list: List[requests.Request], opts: RequestOptions = None):
        """
        Execute the request list and return the list of responses for each request
        
        :param request_list: The list of requests to be executed.
                             i.e: [requests.Request("GET",url="https://google.com")]
        :param opts: The request options (timeouts, etc).
        :return: Returns the response list in an orderly manner.
                 That is, the answer in index n will be in the answer array in position n.
        :see: doc/diagram.png
        """
        if opts is None:
            opts = RequestOptions()
        futures = []
        out: List = [None] * len(request_list)
        with ThreadPoolExecutor(max_workers=opts.workers_count) as executor:
            for i in range(len(request_list)):
                futures.append(executor.submit(Requester._make_request, request_list[i], i, opts.timeout_seconds))
            for future in as_completed(futures):
                (result, id_) = future.result()
                if result is not None:
                    out[id_] = result
        return out
