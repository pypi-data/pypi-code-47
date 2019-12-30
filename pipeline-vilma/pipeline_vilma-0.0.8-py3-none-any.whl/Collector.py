import json
import pymongo
import datetime
import random
from loguru import logger
from pipelinevilma.Messager import Messager


class Collector:
    STATUS_FOR_LABELING = 'labeling-required'

    def __init__(self,  bypass, ratio, queue_server, queue_input, queue_output, database_options):
        self.bypass = bypass
        self.ratio = ratio
        self.queue_output = queue_output
        self.receiver = Messager(queue_server, queue_input)
        self.delivery = Messager(queue_server, queue_output)

        client = pymongo.MongoClient(database_options['url'])
        db = client[database_options['name']]
        self.database_collection = db[database_options['collections']['collector']]

    """Some description that tells you it's abstract,
    often listing the methods you're expected to supply."""

    def run(self):
        self.receive(self.on_new_message)

    def persist(self, message):
        message['createdAt'] = datetime.datetime.utcnow()
        message['status'] = Collector.STATUS_FOR_LABELING
        self.database_collection.insert_one(message)

    def on_new_message(self, ch, method, properties, body):
        # Callback function
        logger.info("Message received!")
        message = json.loads(body)
        sensor_id = message['x']['sensorId']

        if ch.is_open:
            ch.basic_ack(method.delivery_tag)
            random_number = random.random()
            logger.debug(f"Ratio: {self.ratio} Random: {random_number}")
            if not self.bypass and random_number <= self.ratio:
                logger.warning("Persisting image on the database...")
                self.persist(message)
                logger.info("Done!")
            logger.info(f"Forwarding message to queue {self.queue_output}{sensor_id}")
            self.forward(sensor_id, body)
            logger.info("Done!")

    def receive(self, callback):
        self.receiver.consume(callback)

    def forward(self, sensor_id, message):
        self.delivery.publish_to_sibling_queue(message, sensor_id)
