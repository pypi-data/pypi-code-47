# -*- coding: utf8 -*-

from elasticsearch import Elasticsearch
from elasticsearch.client.utils import query_params


class FakeElasticsearch(Elasticsearch):

    @query_params(
        "if_seq_no",
        "if_primary_term",
        "op_type",
        "parent",
        "pipeline",
        "refresh",
        "routing",
        "timeout",
        "timestamp",
        "ttl",
        "version",
        "version_type",
        "wait_for_active_shards")
    def index(self, index, body, doc_type="_doc", id=None, params=None):
        pass
