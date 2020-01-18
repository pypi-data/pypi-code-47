__doc__=f"""mrldb by Rémi "Mr e-RL" LANGDORPH
Copyright (c) 2019 Rémi LANGDORPH - mrerl@warlegend.net
under MIT License (https://github.com/merlleu/mrldb/blob/master/LICENSE)"""

from .struct import get_struct_init
import asyncio
try:
    from mysql.connector.errors import OperationalError
except:
    pass
class MrlDBMsqlAsync:
    def __init__(self, host, database=None, structure=None, user=None, password=None, autocommit=True):
        self.structure=structure
        self._config={"system":"mysql", "host": host, "database": database, "structure": f"{len(structure) if structure!=None else '0'} tables", "user": user, "password":password, "autocommit": autocommit}
        return
    @asyncio.coroutine
    def connect(self):
        import mysql_async.connector as mariadb
        self.connection = mariadb.Connect(host=self._config["host"], database=self._config["database"], user=self._config["user"], password=self._config["password"])
        self.connection.autocommit=self._config["autocommit"]
        yield from self.connection.connect()
        self.cursor = yield from self.connection.cursor()

    @asyncio.coroutine
    def restart(self):
        yield from self.cursor.close()
        yield from self.connection.close()
        import mysql_async.connector as mariadb
        self.connection = mariadb.Connect(host=self._config["host"], database=self._config["database"], user=self._config["user"], password=self._config["password"])
        self.connection.autocommit=self._config["autocommit"]
        yield from self.connection.connect()
        self.cursor = yield from self.connection.cursor()

    @asyncio.coroutine
    def insert(self, table, data):
        def frmt(d):
            return d.__repr__() if d is not None else "null"
        try:
            return (yield from self.cursor.execute(f"INSERT INTO {table}({', '.join([x for x in data.keys()])}) VALUES ({', '.join([frmt(x) for x in data.values()])})"))
        except OperationalError:
            yield from self.restart()
            return (yield from self.cursor.execute(f"INSERT INTO {table}({', '.join([x for x in data.keys()])}) VALUES ({', '.join([frmt(x) for x in data.values()])})"))
    @asyncio.coroutine
    def update(self, table, data, conds=None):
        def frmt(d):
            return d.__repr__() if d is not None else "null"
        try:
            return (yield from self.cursor.execute(f"UPDATE {table} SET {', '.join([key+'='+frmt(arg) for key, arg in data.items()])}{' WHERE '+conds if conds!=None else ''}"))
        except OperationalError:
            yield from self.restart()
            return (yield from self.cursor.execute(f"UPDATE {table} SET {', '.join([key+'='+frmt(arg) for key, arg in data.items()])}{' WHERE '+conds if conds!=None else ''}"))
    @asyncio.coroutine
    def select(self, table, columns, conds=None, nowrap=False):
        if columns=="*":columns=self.structure[table].keys()
        try:
            yield from self.cursor.execute(f"SELECT {'*' if columns=='*' else ', '.join(columns)} FROM {table}{' WHERE '+conds if conds!=None else ''}")
        except OperationalError:
            yield from self.restart()
            yield from self.cursor.execute(f"SELECT {'*' if columns=='*' else ', '.join(columns)} FROM {table}{' WHERE '+conds if conds!=None else ''}")
        if not nowrap:
            return [
            {_col:_var for _col, _var in zip(columns, record)}
            for record in
            (yield from self.cursor.fetchall())
            ]
        else:
            return (yield from self.cursor.fetchall())
    @asyncio.coroutine
    def delete(self, table, conds=None):
        try:
            return (yield from self.cursor.execute(f"DELETE FROM {table}{' WHERE '+conds if conds!=None else ''}"))
        except OperationalError:
            yield from self.restart()
            return (yield from cursor.execute(f"DELETE FROM {table}{' WHERE '+conds if conds!=None else ''}"))
    def _getinfos(self):
        return self._config
    async def init(self):
        [self.cursor.execute(command) for command in get_struct_init(self.structure)]
        return self
    def __str__(self):
        return f"<mrldb.MrlDBMsql at {id(self)} - connection: {self._config['host']}>"
    def __repr__(self):
        return f"<mrldb.MrlDBMsql at {id(self)} - connection: {self._config['host']}>"
