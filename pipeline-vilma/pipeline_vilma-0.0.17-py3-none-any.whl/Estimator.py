from loguru import logger
from pipelinevilma.Messager import Messager
from pipelinevilma.EstimatorActor import EstimatorActor
import os


class Estimator:
    def __init__(self, queue_server, input_queue, output_queue, actor):
        self.input_queue = Messager(queue_server, input_queue)
        self.output_queue = Messager(queue_server, output_queue)
        self.actor = EstimatorActor(actor)

    """Some description that tells you it's abstract,
    often listing the methods you're expected to supply."""

    def run(self):
        logger.info(f"Running Estimator")
        self.consume()

    def estimate(self, ch, method, properties, body):
        if ch.is_open:
            logger.info("Acking message")
            ch.basic_ack(method.delivery_tag)

            logger.info(f"Calling EstimatorActor")
            message = self.actor.estimate(body)
            self.forward(message)

    def consume(self):
        logger.info(f"Consuming from {self.input_queue.queue_name}")
        self.input_queue.consume(self.estimate)

    def forward(self, message):
        logger.info(f"Forwarding message to {self.output_queue.queue_name}")
        self.output_queue.publish(message)
