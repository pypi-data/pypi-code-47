import time
from pipelinevilma.Messager import Messager
from pipelinevilma.packer.BasePackage import BasePackage


class Provider:
    def __init__(self, queue_server, queue_output):
        self.queue = Messager(queue_server, queue_output)

    """Some description that tells you it's abstract,
    often listing the methods you're expected to supply."""

    def pack_data(self, data_type, content, sensor_id):
        raw_data = BasePackage(data_type, content, sensor_id)
        return raw_data.pack()

    def run(self):
        raise NotImplementedError("Should have implemented this")

    def forward(self, message):
        self.queue.publish(message)
