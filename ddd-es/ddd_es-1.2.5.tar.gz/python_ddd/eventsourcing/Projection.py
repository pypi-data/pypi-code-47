"""This module contains classes used to project events."""

import abc
from typing import Any, Dict

from pymongo import MongoClient

from .DomainEventListener import DomainEventListener


class Projection(DomainEventListener):
    """Projection is an abstract class that represent a projection.

    All Projection sub classes must implement `project` method

    """

    def domainEventPublished(self, event: Dict[str, Any]) -> None:  # noqa: D102
        obj_id = event["object_id"]
        event_name = event["event_name"]
        event = event["event"]

        self.project(obj_id, event_name, event)

    @abc.abstractmethod
    def project(self, obj_id: str, event_name: str, event):
        """Project the domain event.

        Args:
            obj_id: the object id
            event_name: the type of event to be projected
            event: the event payload

        Requires:
            No argument is None

        """
        raise NotImplementedError()


class MongoProjection(Projection):
    def __init__(
        self,
        host="localhost",
        port=27017,
        database="fenrys",
        collection="event_store",
        username=None,
        password=None,
    ):
        super().__init__()
        self.__host = host
        self.__port = port
        self.__database_name = database
        self.__collection_name = collection
        self.__username = username
        self.__password = password
        self.collection = None
        self.__db = None
        self.__client = None

    def __enter__(self):
        print("enter")
        if self.__username is not None and self.__password is not None:
            self.__client = MongoClient(
                self.__host,
                self.__port,
                username=self.__username,
                password=self.__password,
            )
        else:
            self.__client = MongoClient(self.__host, self.__port)

        self.__db = self.__client[self.__database_name]
        self.collection = self.__db[self.__collection_name]
        return self.collection

    def __exit__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        print("exit")
        self.__client.close()
        self.__db = None
        self.collection = None

    def domainEventPublished(self, event: Dict[str, Any]) -> None:  # noqa: D102
        # Overrides parent method to establish connection
        with self:
            super().domainEventPublished(event)

    @abc.abstractmethod
    def project(sself, obj_id, event_name, event):  # noqa: D102
        raise NotImplementedError()


class InMemoryProjection(Projection):
    def __init__(self):
        super().__init__()
        self.collection = list()

    @abc.abstractmethod
    def project(self, obj_id, event_name, event):  # noqa: D102
        raise NotImplementedError()
