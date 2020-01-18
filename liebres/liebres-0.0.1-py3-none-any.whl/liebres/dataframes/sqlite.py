from __future__ import annotations

import logging

from .abc import DataFrame
from sqlite3 import (
    connect,
    Connection,
)
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from typing import (
        Dict,
        Type,
        Tuple,
    )

logger = logging.getLogger(__name__)


class SQLiteDataFrame(DataFrame):

    def __init__(self, *args, connection: Connection = None, query: str = None, **kwargs):
        if connection is None:
            connection = connect('database.sqlite')
        super().__init__(connection=connection, *args, **kwargs)
        self.query = query

    TYPE_TO_SQL = {
        str: 'TEXT',
        int: 'INTEGER',
        float: 'REAL',
    }

    SQL_TO_TYPE = {v: k for k, v in TYPE_TO_SQL.items()}

    @property
    def materialized(self) -> bool:
        query = f'SELECT * FROM "sqlite_master" WHERE tbl_name == "{self.table_name}";'
        cursor = self._connection.execute(query)
        return any(cursor.fetchall())

    @property
    def columns(self) -> Dict[str, Type]:
        if not self.materialized:
            self.materialize()
        query = f'SELECT * FROM PRAGMA_TABLE_INFO("{self.table_name}")'
        cursor = self._connection.execute(query)
        raw = cursor.fetchall()

        columns = {row[1]: self.SQL_TO_TYPE[row[2]] for row in raw}
        return columns

    def __len__(self) -> int:
        if not self.materialized:
            self.materialize()
        query = f'SELECT COUNT() FROM "{self.table_name}"'
        cursor = self._connection.execute(query)
        return cursor.fetchone()[0]

    def materialize(self) -> None:
        if self.query is not None:
            self._materialize_from_query()
        elif self._data is not None:
            self._materialize_from_data()

    def _materialize_from_query(self):
        query = self.query
        creation_query = f'CREATE TABLE "{self.table_name}" AS {query}'
        self._connection.execute(creation_query)
        self._connection.commit()

    def _materialize_from_data(self):
        query = f'CREATE TABLE "{self.table_name}" {self._create_columns()};'
        self._connection.execute(query)

        for raw in zip(*self._data.values()):
            self._connection.execute(f'INSERT INTO "{self.table_name}" VALUES ({",".join(map(str, raw))})')
        self._connection.commit()

    def _create_columns(self):
        return "(" + ",".join(f"{k} {v}" for k, v in self._column_database_types.items()) + ")"

    @property
    def _column_types(self) -> Dict[str, Type]:
        if isinstance(self._data, dict):
            return {key: type(values[0]) for key, values in self._data.items()}

        raise NotImplementedError

    @property
    def _column_database_types(self) -> Dict[str, Type]:
        return {key: self.TYPE_TO_SQL[value] for key, value in self._column_types.items()}

    @property
    def _columns(self) -> Tuple[str, ...]:
        return tuple(key for key in self._column_types.keys())

    @property
    def _numeric_columns(self) -> Tuple[str, ...]:
        return tuple(key for key, value in self._column_types.items() if issubclass(value, (int, float)))

    def _head(self, n: int, **kwargs) -> str:
        return f'SELECT * FROM "{self.table_name}" LIMIT {n};'

    def _sum(self, **kwargs) -> str:
        query = f'SELECT {",".join(map(lambda x: f"SUM({x}) AS {x}", self._numeric_columns))} FROM "{self.table_name}";'
        return query

    def _add(self, other: Any, **kwargs) -> str:
        columns = {
            f'"{k}" {"||" if issubclass(v, str) else "+"} {other} AS "{k}"'
            for k, v in self._column_types.items()
        }
        query = f'SELECT {",".join(columns)} FROM "{self.table_name}";'
        return query

    def _subtract(self, other: Any, **kwargs) -> str:
        if any(issubclass(v, str) for v in self._column_types.values()):
            raise TypeError('The given DataFrame has str columns.')

        columns = {
            f'"{k}" - {other} AS "{k}"'
            for k, v in self._column_types.items()
        }
        query = f'SELECT {",".join(columns)} FROM "{self.table_name}";'
        return query

    def _eq(self, other) -> str:
        if isinstance(other, DataFrame):
            raise NotImplementedError
        elif isinstance(other, (int, float, str,)):
            columns = {
                f'"{k}" == {other} AS "{k}"'
                for k, v in self._column_types.items()
            }
            query = f'SELECT {", ".join(columns)} FROM "{self.table_name}";'
            return query
        else:
            raise ValueError

    def _get_item(self, item=None) -> str:
        if item is None:
            column_names = '*'
        elif isinstance(item, str):
            column_names = item
        elif isinstance(item, list):
            column_names = ','.join(item)
        else:
            raise KeyError(item)

        query = f'SELECT {column_names} FROM "{self.table_name}";'
        return query
