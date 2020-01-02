import click
from json import load
from pymongo import MongoClient

from financejson.validate import validate_file
from FinDataBroker.DataBrokerMongoDb import DataBrokerMongoDb
from FinDataBroker.DataBrokerSqlite import DataBrokerSqlite
from FinDataBroker.IndexingMap import indexMap


@click.group()
@click.version_option()
def main():
    pass


@main.command()
@click.argument('file', type=click.Path(exists=True))
@click.argument('mongouri')
@click.argument('dbname')
def write2mongo(**kwargs):
    print(kwargs)
    # check if json file is valid
    validate_file(kwargs['file'])

    # load the data into a dictionary
    with open(kwargs['file'], 'r') as f:
        data = load(f)

    # create a mongodb databroker instance
    client = MongoClient(kwargs['mongouri'])
    dbm = DataBrokerMongoDb(client)

    # write data to mongodb
    # get rid of auxiliary data
    data.pop('yh_symbol')
    data.pop('ms_symbol')
    # loop through the data fielsd
    for k, v in data.items():
        dbm.save(v, db=kwargs['dbname'], col=k, indexTupleList=indexMap[k], unique=True)

    client.close()


@main.command()
@click.argument('file', type=click.Path(exists=True))
@click.argument('sqliteuri')
def write2sqlite(**kwargs):
    # check if json file is valid
    validate_file(kwargs['file'])

    # load the data into a dictionary
    with open(kwargs['file'], 'r') as f:
        data = load(f)

    # create a sqlite databroker instance
    dbs = DataBrokerSqlite(kwargs['sqliteuri'])

    # write data to sqlite
    # get rid of auxiliary data
    data.pop('yh_symbol')
    data.pop('ms_symbol')

    # adapt index map to sql
    indexMapSQL = dict()
    for k, v in indexMap.items():
        _list = []
        for element in v:
            _list.append(element[0])
        indexMapSQL[k] = _list

    # loop through the data fielsd
    for k, v in data.items():
        dbs.save(v, collection=k, indexList=indexMapSQL[k])

    # dbs.db.close()
