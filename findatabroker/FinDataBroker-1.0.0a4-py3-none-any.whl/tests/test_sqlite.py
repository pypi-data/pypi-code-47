import pytest, os
from FinDataBroker.DataBrokerSqlite import DataBrokerSqlite


# @pytest.fixture(scope='function')
# def reset_sqlite_db(request):
#     path = request.param  # Path to database file
#     with open(path, 'w'): pass
#     yield None
#     os.remove(path)

# @pytest.fixture(autouse=True)
# def reset(reset_sqlite_db):
#     reset_sqlite_db.reset()

@pytest.fixture(scope='function')
def db(tmpdir):
    file = os.path.join("sqlite:///test.db")
    print(file)
    yield file
    os.remove('test.db')


# @pytest.mark.parametrize('reset_sqlite_db', ['/tmp/test_db.sql'], indirect=True)
def test_create_database_no_tables___ok(db):
    dbsql = DataBrokerSqlite(db)

    assert dbsql.db.tables == []


# @pytest.mark.parametrize('reset_sqlite_db', ['/tmp/test_db.sql'], indirect=True)
def test_create_database_create_table___ok(db):
    dbsql = DataBrokerSqlite(db)
    dbsql.save({}, 'test', ['year'])

    assert dbsql.db.tables == ['test']
    assert len(dbsql.db['test']) == 1


def test_create_database_create_table_with_data__ok(db):
    dbsql = DataBrokerSqlite(db)
    dbsql.save({"boe": "hallo"}, 'test', ['boe'])

    assert dbsql.db.tables == ['test']
    assert dbsql.db["test"].columns == ['id', "boe"]
    assert len(dbsql.db["test"]) == 1

    dbsql.save({"year": 2019}, 'test', ['boe', 'year'])

    assert len(dbsql.db["test"]) == 2
    assert dbsql.db["test"].columns == ['id', "boe", 'year']

    boe = dbsql.db['test'].find_one(boe="hallo")

    assert boe["boe"] == "hallo"


def test_load_ok(db):
    dbsql = DataBrokerSqlite(db)
    dbsql.save({"boe": "hallo"}, 'test', ['boe'])

    assert dbsql.db.tables == ['test']
    assert dbsql.db["test"].columns == ['id', "boe"]
    assert len(dbsql.db["test"]) == 1

    dbsql.save({"year": 2019}, 'test', ['boe', 'year'])
    retrieved = dbsql.load('test', {'boe': 'hallo'})
    assert len(retrieved) == 1
    assert retrieved[0]['boe'] == 'hallo'

    dbsql.save({"year": 2019}, 'test', ['boe', 'year'])
    retrieved = dbsql.load('test', {'boe': 'hallo'})
    assert len(retrieved) == 1
    assert retrieved[0]['boe'] == 'hallo'
    assert len(dbsql.db["test"]) == 2
