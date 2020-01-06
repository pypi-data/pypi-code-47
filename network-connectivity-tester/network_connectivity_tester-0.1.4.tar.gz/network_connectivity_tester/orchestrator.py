import boto3
import botocore
import logging
import time
import json
import uuid
from contextlib import contextmanager

LOG = logging.getLogger(__name__)


class ConnectivityTestOrchestrator(object):
    def __init__(self, queue_name="connectivitytest", sqs_region="us-east-2"):
        self.queue_name = "%s-%s" % (queue_name, uuid.uuid1())
        self._timeout = 20
        self._registered_instances = {}
        self._response_tracker = {}
        self._name_to_instance_map = {}
        self._instance_to_name_map = {}
        self.sqs = boto3.resource("sqs", region_name=sqs_region)

        try:
            # Get the queue. This returns an SQS.Queue instance
            self.registration_queue = self.sqs.get_queue_by_name(
                QueueName=self.queue_name
            )

            assert self.registration_queue.url
        except botocore.exceptions.ClientError as err:
            self.registration_queue = self.sqs.create_queue(QueueName=self.queue_name)

    def cleanup(self):
        self.registration_queue.delete()
        for instance_id, instance_info in self._registered_instances.items():
            instance_info["command_queue"].delete()

    def instance_str(self, instance_id):
        return "%s (%s)" % (instance_id, self._instance_to_name_map[instance_id])

    def receive(self, max_number=1):
        messages = self.registration_queue.receive_messages(
            AttributeNames=["All"],
            MaxNumberOfMessages=max_number,
            MessageAttributeNames=["All"],
            WaitTimeSeconds=self._timeout,
        )

        return messages

    def send_command(self, instance, command, value):
        instance_id = self._name_to_instance_map[instance]

        res = self._registered_instances[instance_id]["command_queue"].send_message(
            MessageBody="Connection Test: %s" % value,
            MessageAttributes={
                command: {"StringValue": value, "DataType": "String.Command"}
            },
        )

        self._response_tracker[res["MessageId"]] = False
        LOG.info("Sent %s %s to %s" % (command, value, self.instance_str(instance_id)))

    def wait_for_registrations(self, instance_ids=None, instances=None, max_retry=20):
        """
        Try to register ec2 instances for connection testing. Those instances must run the python tooling and
        initiate the registration process, we just wait for all of them. Returns false if not all of them registered.

        :param instance_ids: List of instance ids that we want to use for testing OR
        :type list
        :param instances:  Dict of name: instance id pairs that we want to use for testing
        :type dict
        :param max_retry: Max number of retries till the method polls SQS
        :type int
        :return: bool
        """
        if not instance_ids and instances:
            instance_ids = [instance[1] for instance in instances.items()]
            self._name_to_instance_map = instances
        else:
            self._name_to_instance_map = {
                instance_id: instance_id for instance_id in instance_ids
            }
        self._instance_to_name_map = {
            value: key for key, value in self._name_to_instance_map.items()
        }
        self._registered_instances = {
            instance_id: False for instance_id in instance_ids
        }

        LOG.info("Waiting for instance registrations: %s" % instance_ids)
        i = 0
        while i < max_retry:
            i = i + 1

            LOG.info("Receiving registration messages from SQS")
            messages = self.receive(10)
            if messages:
                for message in messages:
                    if "InstanceRegistration" not in message.message_attributes:
                        continue

                    instance_id = message.message_attributes["InstanceRegistration"][
                        "StringValue"
                    ]
                    if instance_id in instance_ids:
                        self._registered_instances[instance_id] = json.loads(
                            message.body
                        )

                        self._registered_instances[instance_id][
                            "command_queue"
                        ] = self.sqs.get_queue_by_name(
                            QueueName=self._registered_instances[instance_id][
                                "command_queue_name"
                            ]
                        )

                        LOG.info(
                            "Instance %s (%s) successfully registered"
                            % (self._instance_to_name_map[instance_id], instance_id)
                        )

                        message.delete()

                    if all([el[1] for el in self._registered_instances.items()]):
                        return True

            if i >= 5:
                time.sleep(10)

        return False

    def wait_for_response(self, max_retry=20):
        LOG.info("Waiting for instances to respond")

        i = 0
        while i < max_retry:
            i = i + 1

            messages = self.receive(10)
            if messages:
                for message in messages:
                    if "CommandStatus" not in message.message_attributes:
                        continue

                    instance_id = message.message_attributes["InstanceId"][
                        "StringValue"
                    ]
                    command_message_id = message.message_attributes["CommandMessageId"][
                        "StringValue"
                    ]
                    status = message.message_attributes["CommandStatus"]["StringValue"]
                    body = message.body

                    if command_message_id in self._response_tracker:
                        self._response_tracker[command_message_id] = True
                        message.delete()
                    else:
                        continue

                    if status != "Success":
                        LOG.error(
                            "Got message response %s (%s) from %s"
                            % (status, body, self.instance_str(instance_id))
                        )
                        return False

                    LOG.info(
                        "Got message response %s from %s"
                        % (status, self.instance_str(instance_id))
                    )
                    if all([el[1] for el in self._response_tracker.items()]):
                        return True

            if i >= 5:
                time.sleep(10)

        return False

    def get_instance_ips(self, instance, public=False):
        instance_id = self._name_to_instance_map[instance]

        nic_config = self._registered_instances[instance_id]["nic_config"]
        if public:
            ip_list = nic_config["ipv4-associations"]
        else:
            ip_list = nic_config["local-ipv4s"]

        return ip_list

    def test_url(self, instance, url, batch=False):
        self.send_command(instance=instance, command="ConnectURL", value=url)

        if batch:
            return True
        return self.wait_for_response()

    def test_ping_internal(self, source, destination, batch=False):
        for destination_ip in self.get_instance_ips(destination):
            self.send_command(instance=source, command="Ping", value=destination_ip)

        if batch:
            return True
        return self.wait_for_response()

    def test_tcp(self, source, destination, port, public=False):
        self.send_command(instance=destination, command="Listen", value=str(port))
        self.wait_for_response()

        for destination_ip in self.get_instance_ips(destination, public=public):
            address = "%s:%d" % (destination_ip, port)
            self.send_command(instance=source, command="ConnectTCP", value=address)

        return self.wait_for_response()


@contextmanager
def connectivity_tester():
    connectivity_test_object = ConnectivityTestOrchestrator()

    try:
        yield connectivity_test_object
    finally:
        connectivity_test_object.cleanup()
