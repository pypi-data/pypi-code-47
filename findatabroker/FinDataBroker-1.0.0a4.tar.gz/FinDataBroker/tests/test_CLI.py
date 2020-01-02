from json import dump

import dataset
from click.testing import CliRunner
from financejson.validate import validate_file
from pymongo import MongoClient
from FinDataBroker.CLI import write2mongo, write2sqlite


def test_write2mongo_invalid_CLI():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(write2mongo, ['test.json', 'boe'])
        assert result.exit_code == 2


def test_write2mongo_no_valid_file_does_not_exist():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(write2mongo, ['test.json', 'boe', 'boe'])
        assert result.exit_code == 2


def test_write2mongo_invalid_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        data = {
            "yh_symbol": [{"symbol": "XYZ"}]
        }
        with open('test.json', 'w') as f:
            dump(data, f)
        result = runner.invoke(write2mongo, ['test.json', 'boe', 'boe'])
        assert result.exit_code == 1

# def test_write2mongo_valid_file():
#     runner = CliRunner()
#
#     with runner.isolated_filesystem():
#         data = {
#             "yh_symbol": [{"symbol": "AAPL"}],
#             "ms_symbol": [{"symbol": "US_AAPL"}],
#             "yh_assetProfile": [
#                 {
#                     "index_symbol": "XYZ",
#                     "date": "2019-01-01",
#                     "address1": "foo",
#                     "auditRisk": 1,
#                     "boardRisk": 2,
#                     "city": "bar",
#                     "country": "a"
#                 }],
#         }
#
#         with open('test.json', 'w') as f:
#             dump(data, f)
#         validate_file('test.json')
#         result = runner.invoke(write2mongo, ['test.json', 'localhost:27017', 'boe'])
#         assert result.exit_code == 0
#
#         client = MongoClient('localhost:27017')
#
#         stored = list(client['boe']['yh_assetProfile'].find({}))
#         for elem in stored:
#             elem.pop('_id')
#
#         assert data['yh_assetProfile'] == stored
#
#         client.drop_database('boe')
#         client.close()


def test_write2sqlite_invalid_CLI():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(write2mongo, ['test.json'])
        assert result.exit_code == 2


def test_write2sqlite_no_valid_file_does_not_exist():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(write2mongo, ['test.json', 'boe'])
        assert result.exit_code == 2


def test_write2sqlite_invalid_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        data = {
            "yh_symbol": [{"symbol": "XYZ"}]
        }
        with open('test.json', 'w') as f:
            dump(data, f)
        result = runner.invoke(write2mongo, ['test.json', 'boe'])
        assert result.exit_code == 2


def test_write2sqlite_valid_file():
    runner = CliRunner()

    with runner.isolated_filesystem():
        data = {
            "yh_symbol": [{"symbol": "AAPL"}],
            "ms_symbol": [{"symbol": "US_AAPL"}],
            "yh_assetProfile": [
                {
                    "index_symbol": "XYZ",
                    "date": "2019-01-01",
                    "address1": "foo",
                    "auditRisk": 1,
                    "boardRisk": 2,
                    "city": "bar",
                    "country": "a"
                }],
        }

        with open('test.json', 'w') as f:
            dump(data, f)
        validate_file('test.json')

        result = runner.invoke(write2sqlite, ['test.json', 'sqlite:///test.db'])
        assert result.exit_code == 0

        db = dataset.connect('sqlite:///test.db')
        stored = list(db['yh_assetProfile'])

        for elem in stored:
            elem.pop('id')
        assert data['yh_assetProfile'] == stored
