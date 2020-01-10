from __future__ import print_function

import grpc
from annoyclients import index_pb2_grpc, index_pb2
import time

BATCH_SIZE = 100


class AnnoyClient:

    def __init__(self, URI):
        channel = grpc.insecure_channel(URI)
        self.stub = index_pb2_grpc.IndexStub(channel)

    def add_documents(self, indexing_items):
        indexRequest = index_pb2.IndexRequest()
        start_time = time.time() * 1000

        for index in range(len(indexing_items)):
            item = indexing_items[index]

            vectorLabel = indexRequest.vectorLabels.add()
            vectorLabel.label = str(item[0])
            map(lambda value: vectorLabel.vector.append(value), item[1])

            if index > 0 and index % BATCH_SIZE == 0:
                self.stub.index(indexRequest)
                indexRequest = index_pb2.IndexRequest()

        if len(indexRequest.vectorLabels) > 0:
            self.stub.index(indexRequest)
        end_time = time.time() * 1000
        print("Indexing Time: " + str(end_time - start_time))

    def get_nearest(self, search_item, number_of_result):
        start_time = time.time() * 1000
        queryRequest = index_pb2.QueryRequest()
        map(lambda item: queryRequest.vector.append(item), search_item)
        queryRequest.numberOfResults = number_of_result
        end_time = time.time() * 1000
        print("Query Time: " + str(end_time - start_time))
        results = self.stub.query(queryRequest)
        return results.queryResults

    def build(self):
        buildRequest = index_pb2.BuildRequest()
        buildRequest.numberOfTree = 10
        self.stub.build(buildRequest)
