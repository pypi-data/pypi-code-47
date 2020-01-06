from elasticsearch import Elasticsearch
from tv2test.constants import ConstElk
from abc import ABCMeta, abstractmethod


class ELKDocMapping(metaclass=ABCMeta):
    @property
    @abstractmethod
    def _doc_mapping(self):
        pass
    @abstractmethod
    def get_doc_mapping(self, doc_type:object):
        pass
    @_doc_mapping.setter
    @abstractmethod
    def _doc_mapping(self, value):
        pass


class ELKBellDocMapping(ELKDocMapping):
    def __init__(self):
        self.const_elk = ConstElk()
        
    @property
    def _doc_mapping(self):
        return {
            self.const_elk.DOC_TEST_DETAILS: {
                "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0
                },
                "mappings": {
                    self.const_elk.DOC_TEST_DETAILS: {
                        "dynamic": "strict",
                        "properties": {
                            "name": {
                                "type": "text"
                            },
                            "pass_status": {
                                "type": "boolean"
                            },
                            "completion_time": {
                                "type": "double"
                            },
                            "setup_box_acct_no": {
                                "type": "text"
                            },
                            "setup_box_device_code": {
                                "type": "text"
                            },
                            "setup_box_id": {
                                "type": "text"
                            },
                            "video_url": {
                                "type": "text"
                            },
                            "pass_percentage": {
                                "type": "integer"
                            },
                            "type": {
                                "type": "text"
                            },
                            "device_type": {
                                "type": "text"
                            },
                            "host_name": {
                                "type": "text"
                            },
                            "user_name": {
                                "type": "text"
                            },
                            "fail_reason": {
                                "type": "text"
                            },
                            "timestamps": {
                                "dynamic": "true",
                                "type": "nested"
                             },
                            "durations": {
                                "dynamic": "true",
                                "type": "nested"
                            },
                            "created": {
                                "type": "date"
                            }
                        }
                    }
                }
            }
        }

    def get_doc_mapping(self, doc_type: str):
        if doc_type in self._doc_mapping:
            return self._doc_mapping[doc_type]
        return None


class ELKBell:
    def __init__(self, index_name: str, doc_type: str, elk_mapping: ELKDocMapping):
        self._es = None
        if self.connect():
            self.index_name = index_name
            self.doc_type = doc_type

            #self.delete_index(index_name=index_name)
            if not self.is_index_exist(index_name= index_name):
                doc_mapping = elk_mapping.get_doc_mapping(doc_type=doc_type)

                if doc_mapping is not None:
                    if not self.create_index(doc_mapping=doc_mapping):
                        raise Exception("Not able to create index")
                else:
                    raise Exception("No doc type found for given index name.")
        else:
            raise Exception("Not able to connect with elastic search instance.")

    def connect(self):
        self._es = Elasticsearch([{'host': 'localhost', 'port': 9200}], http_auth=('elastic', 'Password!'))
        if self._es.ping():
            return True
        return False

    def is_index_exist(self, index_name: str):
        return self._es.indices.exists(index_name)

    def create_index(self, doc_mapping: object):
        try:
            self._es.indices.create(index=self.index_name, body=doc_mapping)
            return True
        except Exception as ex:
            print("Exception:- ", str(ex))
            return False
        finally:
            return True

    def insert_data(self, data: object):
        try:
            res = self._es.index(index=self.index_name, doc_type=self.doc_type, body=data)
            print("Index Data Response:- ", res)
            return True
        except Exception as ex:
            print("Exception:- ",ex)
        return False

    def delete_index(self, index_name: str):
        self._es.indices.delete(index=index_name, ignore=[400, 404])
