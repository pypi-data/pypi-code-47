import abc
import json
import os
import time
import uuid

from typing import *

import boto3
import zstandard as zstd
from grapl_graph_descriptions_py.graph import Graph
from grapl_graph_descriptions_py.graph_description_pb2 import GeneratedSubgraphs


class SqsClient(object):
    def __init__(self, queue_url: str):
        self._queue_url = queue_url
        self._sqs_client = boto3.resource('sqs')

    def ack_event(self, receipt_handle: str):
        self._sqs_client.delete_message(
            QueueUrl=self._queue_url,
            ReceiptHandle=receipt_handle
        )


class Generator(abc.ABC):
    @abc.abstractmethod
    def generate_graphs(self, event: bytes) -> List[Graph]:
        pass


class GeneratorHarness(object):
    def __init__(
            self,
            queue_url=None,  # type: Optional[str]
            output_bucket=None,  # type: Optional[str]
    ) -> None:
        self._sqs_client = SqsClient(queue_url or os.environ['QUEUE_URL'])  # type: SqsClient
        self._output_bucket = output_bucket or os.environ['OUTPUT_BUCKET']
        self._region = ""
        self._payload_retriever = S3PayloadRetriever()
        self._payload_decoder = ZstdDecoder()
        self._payload_encoder = ZstdProtoEncoder()
        self._payload_emitter = S3PayloadEmitter(self._output_bucket)
        self._cache = None

    def run(
            self,
            event,
            context,
            generator,
    ):
        for event in event['Records']:
            s3_event = json.loads(event['body'])['s3']
            bucket, key = (
                s3_event['bucket']['name'],
                s3_event['object']['key'],
            )

            encoded_payload = self._payload_retriever.fetch_payload(bucket, key)
            decoded_payload = self._payload_decoder.decode(encoded_payload)

            # Call the generator, TODO: Handle exceptions
            graphs = generator.generate_graphs(decoded_payload)

            # Encode output
            encoded_graphs = self._payload_encoder.encode(graphs)

            # Emit output event
            self._payload_emitter.emit(encoded_graphs)

            # Ack the event
            self._sqs_client.ack_event(event['receiptHandle'])
        # generator.generate_graphs()


class ZstdDecoder(object):
    def decode(self, input: bytes) -> bytes:
        dctx = zstd.ZstdDecompressor()
        return dctx.decompress(input)


class ZstdProtoEncoder(object):
    def encode(self, graphs: List[Graph]) -> bytes:
        cctx = zstd.ZstdCompressor()
        return cctx.compress(GeneratedSubgraphs(graphs))


class S3PayloadRetriever(object):
    def __init__(self):
        self.s3_connection = boto3.resource('s3')

    def fetch_payload(self, bucket: str, key: str) -> bytes:
        obj = self.s3_connection.Object(bucket, key)
        # TODO: Read into buffer, prellocate with the object size
        return obj.get()['Body'].read()


class S3PayloadEmitter(object):
    def __init__(self, bucket):
        self.s3_connection = boto3.resource('s3')
        self.bucket = bucket

    def emit(self, event: bytes):
        t = int(time.time())
        day = t - (t % 86400)
        u = str(uuid.uuid4())
        key = f"{day}/{t}-{u}"

        obj = self.s3_connection.Object(self.bucket, key)
        obj.put(Body=event)

