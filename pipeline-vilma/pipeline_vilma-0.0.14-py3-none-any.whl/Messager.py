import pika


class Messager:
    def __init__(self, server_url, queue_name):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(server_url)
        )
        self.queue_name = queue_name
        self.channel = connection.channel()
        self.channel.queue_declare(queue=queue_name)

    def publish_to_sibling_queue(self, message, unique_id):
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue_name + str(unique_id),
                                   body=message)

    def publish(self, message, exchange=''):
        self.channel.basic_publish(exchange=exchange,
                                   routing_key=self.queue_name,
                                   body=message)

    def get_message(self):
        method_frame, header_frame, body = self.channel.basic_get(self.queue_name)
        if method_frame:
            self.channel.basic_ack(method_frame.delivery_tag)
            return body
        else:
            return False

    def consume(self, callback):
        self.channel.basic_consume(queue=self.queue_name,
                                   on_message_callback=callback,
                                   auto_ack=False)
        self.channel.start_consuming()
