import pytest
from pytest import raises
import mongomock
from pymongo import ASCENDING
from FinDataBroker.DataBrokerMongoDb import DataBrokerMongoDb

client = mongomock.MongoClient()
broker = DataBrokerMongoDb(client)


def test___databroker_creation___ok():
    assert isinstance(broker, DataBrokerMongoDb)


# not implemented in mongomock
# def test___get_stat_non_existing_db___nog():
#     with raises(AttributeError):
#         broker.get_stats('test')

def test__save___ok():
    db = 'testdb'
    col = 'testcol'
    objs = [
        {
            'name': 'boe',
            'year': 2019
        }
    ]
    index = [('name', ASCENDING), ('year', ASCENDING)]

    broker.save(objs, db, col, index, unique=True)
    assert broker.get_number_of_documents(db, col) == 1


def test__load___ok():
    db = 'testdb'
    col = 'testcol'
    objs = [
        {
            'name': 'boe',
            'year': 2019
        }
    ]
    index = [('name', ASCENDING), ('year', ASCENDING)]

    broker.save(objs, db, col, index, unique=True)
    assert broker.get_number_of_documents(db, col) == 1

    data = broker.load(db, col, {'year': 2019})
    assert objs == data
