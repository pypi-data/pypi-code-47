# coding: utf-8
from concurrent.futures import ThreadPoolExecutor
from tornado import web
from tornado.concurrent import run_on_executor
from tornado.gen import coroutine


@web.stream_request_body
class ChunkHTTPHandler(web.RequestHandler):
    executor = ThreadPoolExecutor(max_workers=4)

    def prepare(self):
        self.task_id = self.request.headers['task_id']
        self.no = 0

    @run_on_executor
    def handle_chunk(self, chunk, chunk_no):
        raise NotImplementedError()

    def data_received(self, chunk):
        self.no += 1
        return self.handle_chunk(chunk, self.no)

    @coroutine
    def post(self):
        self.finish('{} chunks received, task id is {}'.format(self.no, self.task_id))
