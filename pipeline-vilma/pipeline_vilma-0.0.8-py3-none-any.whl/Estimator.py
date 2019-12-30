from loguru import logger
from pipelinevilma.Messager import Messager


class Estimator:
    def __init__(self, queue_server, input_queue, output_queue):
        self.input_queue = Messager(queue_server, input_queue)
        self.output_queue = Messager(queue_server, output_queue)

    """Some description that tells you it's abstract,
    often listing the methods you're expected to supply."""

    def run(self):
        raise NotImplementedError("Should have implemented this")

    def estimate(self):
        raise NotImplementedError("Should have implemented this")

    def consume(self):
        self.input_queue.consume(self.estimate)

    def forward(self, message):
        self.output_queue.publish(message)
