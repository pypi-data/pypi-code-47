import json
import logging
import subprocess

import boto3
import botocore
import urllib.request
from cached_property import cached_property

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()


class AWSConnectivityTestClient(object):
    def __init__(self, region=None, registration_queue_name=None):
        self.region = region
        self.command_queue_name = "%s-%s" % (registration_queue_name, self.instance_id)
        self.registration_queue_name = registration_queue_name

        self.registration_queue = None
        self.command_queue = None

        # list of ports socat is running on
        self._listen = {}

        self.register()

    @cached_property
    def sqs(self):
        return boto3.resource("sqs", region_name=self.region)

    @cached_property
    def instance_id(self):
        return (
            urllib.request.urlopen(
                "http://169.254.169.254/latest/meta-data/instance-id"
            )
            .read()
            .decode()
        )

    @cached_property
    def nic_macs(self):
        return [
            mac.decode().strip("/")
            for mac in urllib.request.urlopen(
                "http://169.254.169.254/latest/meta-data/network/interfaces/macs"
            ).readlines()
        ]

    @cached_property
    def nic_config(self):
        nic_config = {}

        for mac in self.nic_macs:
            nic_config["vpc-id"] = (
                urllib.request.urlopen(
                    "http://169.254.169.254/latest/meta-data/network/interfaces/macs/%s/vpc-id"
                    % mac
                )
                .read()
                .decode(),
            )
            nic_config["security-groups"] = (
                [
                    el.decode()
                    for el in urllib.request.urlopen(
                        "http://169.254.169.254/latest/meta-data/network/interfaces/macs/%s/security-groups"
                        % mac
                    ).readlines()
                ],
            )

            try:
                nic_config["ipv4-associations"] = [
                    el.decode()
                    for el in urllib.request.urlopen(
                        "http://169.254.169.254/latest/meta-data/network/interfaces/macs/%s/ipv4-associations"
                        % mac
                    ).readlines()
                ]
            except urllib.error.HTTPError:
                pass

            try:
                nic_config["local-ipv4s"] = [
                    el.decode()
                    for el in urllib.request.urlopen(
                        "http://169.254.169.254/latest/meta-data/network/interfaces/macs/%s/local-ipv4s"
                        % mac
                    ).readlines()
                ]
            except urllib.error.HTTPError:
                pass

        return nic_config

    def register(self):
        try:
            # Get the queue. This returns an SQS.Queue instance
            self.registration_queue = self.sqs.get_queue_by_name(
                QueueName=self.registration_queue_name
            )

            # You can now access identifiers and attributes
            assert self.registration_queue.url
        except botocore.exceptions.ClientError as err:
            self.registration_queue = self.sqs.create_queue(
                QueueName=self.registration_queue_name
            )

        self.command_queue = self.sqs.create_queue(QueueName=self.command_queue_name)

        registration_payload = {
            "instance_id": self.instance_id,
            "command_queue_name": self.command_queue_name,
            "command_queue_url": self.command_queue.url,
            "nic_config": self.nic_config,
        }

        self.registration_queue.send_message(
            MessageBody=json.dumps(registration_payload),
            MessageAttributes={
                "InstanceRegistration": {
                    "StringValue": self.instance_id,
                    "DataType": "String",
                }
            },
        )

    def response(self, success, body, message_id):
        LOG.info("Sending response %s to message %s" % (success, message_id))
        self.registration_queue.send_message(
            MessageBody=body,
            MessageAttributes={
                "CommandStatus": {
                    "StringValue": "Success" if success else "Error",
                    "DataType": "String",
                },
                "InstanceId": {"StringValue": self.instance_id, "DataType": "String"},
                "CommandMessageId": {"StringValue": message_id, "DataType": "String"},
            },
        )

    @staticmethod
    def socat(port):
        cmd = (
            '/usr/bin/socat -vv TCP-LISTEN:%d,crlf,reuseaddr,fork SYSTEM:"echo HTTP/1.0 200; echo Content-Type\: text/plain; echo; echo OK %d"'
            % (port, port)
        )
        LOG.info(cmd)

        proc = subprocess.Popen(cmd, shell=True)

        if proc.returncode:
            cout, cerr = proc.communicate()
            raise subprocess.CalledProcessError(
                returncode=proc.returncode, cmd=cmd, output=cout, stderr=cerr
            )

        return proc.pid

    @staticmethod
    def ping_check(address):
        cmd = "ping -c 5 %s" % address
        LOG.info(cmd)

        subprocess.run(cmd.split(), check=True)

        return True

    @staticmethod
    def tcp_check(address):
        url = "http://%s" % address
        LOG.info("Connecting to %s" % url)

        res = urllib.request.urlopen(url).readline().decode().strip()

        if res == "OK %s" % address.split(":")[1]:
            LOG.info("Result OK")

            return True
        return False

    @staticmethod
    def url_check(url):
        LOG.info("Connecting to %s" % url)

        res = urllib.request.urlopen(url)

        if res.status == 200:
            LOG.info("Result OK")

            return True
        return False

    def handle(self, message):
        commands = [
            (cmd, args["StringValue"])
            for cmd, args in message.message_attributes.items()
            if args["DataType"] == "String.Command"
        ]

        for cmd in commands:
            try:
                if cmd[0] == "Listen":
                    LOG.info("Listen on %d" % int(cmd[1]))
                    if cmd[1] not in self._listen:
                        pid = self.socat(int(cmd[1]))
                        self._listen[cmd[1]] = pid

                    self.response(
                        success=True, body=message.body, message_id=message.message_id
                    )

                if cmd[0] == "ConnectTCP":
                    res = self.tcp_check(cmd[1])

                    if res:
                        self.response(
                            success=True,
                            body=message.body,
                            message_id=message.message_id,
                        )

                if cmd[0] == "Ping":
                    res = self.ping_check(cmd[1])

                    if res:
                        self.response(
                            success=True,
                            body=message.body,
                            message_id=message.message_id,
                        )

                if cmd[0] == "ConnectURL":
                    res = self.url_check(cmd[1])

                    if res:
                        self.response(
                            success=True,
                            body=message.body,
                            message_id=message.message_id,
                        )
            except Exception as e:
                self.response(success=False, body=str(e), message_id=message.message_id)

    def loop(self):
        while True:
            LOG.info("Polling %s" % self.command_queue.url)
            response = self.command_queue.receive_messages(
                AttributeNames=["All"],
                MaxNumberOfMessages=1,
                MessageAttributeNames=["All"],
                WaitTimeSeconds=20,
            )
            try:
                try:
                    self.handle(message=response[0])
                    response[0].delete()
                except AttributeError:
                    LOG.info("Deleting ", response[0].receipt_handle)
                    response[0].delete()
            except (KeyError, IndexError):
                LOG.warning(response)
