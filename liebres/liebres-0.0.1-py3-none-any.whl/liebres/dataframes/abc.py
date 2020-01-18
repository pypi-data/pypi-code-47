from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from uuid import uuid4
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import (
        Union,
        Iterable,
        Dict,
        Any,
        Tuple,
    )

logger = logging.getLogger(__name__)


class DataFrame(ABC):

    def __new__(cls, *args, **kwargs) -> DataFrame:
        if cls is DataFrame:
            from .sqlite import SQLiteDataFrame
            cls = SQLiteDataFrame
        self = object.__new__(cls)
        return self

    def __init__(self, data: Union[Iterable, Dict, DataFrame] = None, table_name: str = None, connection=None,
                 *args, **kwargs):
        self._data = data

        self._connection = connection
        self._table_name = table_name
        self._uuid = uuid4()

    @property
    def table_name(self) -> str:
        return self._table_name if self._table_name else str(self._uuid)

    @property
    @abstractmethod
    def materialized(self) -> bool:
        pass

    @abstractmethod
    def materialize(self) -> None:
        pass

    def head(self, n: int = 5) -> DataFrame:
        if not self.materialized:
            self.materialize()
        query = self._head(n=n)
        return self.__class__(connection=self._connection, query=query)

    @abstractmethod
    def _head(self, n: int, **kwargs) -> str:
        pass

    @property
    @abstractmethod
    def columns(self) -> Dict[str, Any]:
        pass

    @property
    def shape(self) -> Tuple[int, int]:
        return len(self), len(self.columns)

    @abstractmethod
    def __len__(self) -> int:
        pass

    def sum(self):
        if not self.materialized:
            self.materialize()
        query = self._sum()
        cursor = self._connection.execute(query)
        raw = cursor.fetchone()
        names = list(map(lambda x: x[0], cursor.description))
        return dict(zip(names, raw))

    @abstractmethod
    def _sum(self, **kwargs) -> str:
        pass

    def __add__(self, other) -> DataFrame:
        return self.add(other)

    def add(self, other) -> DataFrame:
        if not self.materialized:
            self.materialize()
        query = self._add(other=other)
        return self.__class__(connection=self._connection, query=query)

    @abstractmethod
    def _add(self, other, **kwargs) -> str:
        pass

    def __sub__(self, other) -> DataFrame:
        return self.subtract(other)

    def subtract(self, other) -> DataFrame:
        if not self.materialized:
            self.materialize()
        query = self._subtract(other=other)
        return self.__class__(connection=self._connection, query=query)

    @abstractmethod
    def _subtract(self, other, **kwargs) -> str:
        pass

    def to_dict(self, orient: str = 'dict'):
        if not self.materialized:
            self.materialize()

        query = self._get_item()
        cursor = self._connection.execute(query)
        raw = cursor.fetchall()
        names = list(map(lambda x: x[0], cursor.description))

        if orient == 'dict':
            iterable = zip(*raw)
            iterable = list(map(lambda x: dict(enumerate(x)), iterable))
            iterable = zip(names, iterable)
            return dict(iterable)
        if orient == 'list':
            iterable = zip(*raw)
            iterable = zip(names, list(iterable))
            return dict(iterable)
        if orient == 'records':
            return [dict(zip(names, row)) for row in raw]
        raise NotImplementedError

    def __eq__(self, other):
        return self.eq(other)

    def eq(self, other) -> DataFrame:
        if not self.materialized:
            self.materialize()

        query = self._eq(other=other)
        return self.__class__(
            connection=self._connection,
            query=query,
        )

    @abstractmethod
    def _eq(self, other) -> str:
        pass

    def equals(self, other: DataFrame) -> bool:
        return self.to_dict() == other.to_dict()

    def __getitem__(self, item):
        if not self.materialized:
            self.materialize()
        query = self._get_item(item)
        return self.__class__(connection=self._connection, query=query)

    @abstractmethod
    def _get_item(self, item=None) -> str:
        pass

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '\n'.join(map(str, self.to_dict('records')))
