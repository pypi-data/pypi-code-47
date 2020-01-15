"""
# The definition of the Microservice host object
"""
import importlib
import inspect
import logging
from collections import defaultdict
from traceback import format_exc
from typing import TypeVar
from celery.utils.log import get_task_logger

import celery as celery
import graphene as g
import msgpack

from metamorphosis.events import ExceptionEvent, dump_objecttype, load_objecttype
E = TypeVar('E', bound=Exception)

class ConsumerGroup:
    """
    A group of consumer functions that are run inside of a single process.

    Do not create this directly. Instead create these objects through Microservice().consumer_group(...)
    or the @microservice.event_consumer() decorator.
    """

    def __init__(self, microservice):
        self.microservice = microservice
        self.event_consumers = defaultdict(list)
        self.logger = microservice.logger

    def consume_event(self, src_evt):
        ret = None
        for evt_class in self.event_consumers:
            self.logger.debug(f"Checking to see if {src_evt} is an instance of {evt_class}")
            if isinstance(src_evt, evt_class):
                self.logger.debug(f"Yep. Going through consumers")
                for is_generator, save_result_for_sync_mutation, fn in self.event_consumers[evt_class]:
                    self.logger.debug(f"{is_generator} {save_result_for_sync_mutation} {fn}")
                    try:
                        if not is_generator:  # if the function is not a generator
                            rsp_evt = fn(src_evt)  # call it
                            if rsp_evt:  # if it returned a value,
                                if isinstance(rsp_evt, tuple):
                                    t, rsp_evt = rsp_evt
                                else:
                                    t = self.microservice.name
                                if save_result_for_sync_mutation:
                                    ret = dump_objecttype(rsp_evt)

                                self.logger.debug("Sending event to %s, %s", t, rsp_evt)
                                self.consume_event(rsp_evt)
                                self.logger.debug("Call is finished.")
                        else:  # otherwise, every yielded object should be an event
                            rsp_evt = None
                            for rsp_evt in fn(src_evt):  # for each yielded object,
                                if isinstance(rsp_evt, tuple):
                                    t, rsp_evt = rsp_evt
                                else:
                                    t = self.microservice.name
                                self.logger.debug("Sending event to %s, %s", t, rsp_evt)
                                self.consume_event(rsp_evt)  # send it on the bus, but it's not a "result"

                            if save_result_for_sync_mutation:
                                ret = dump_objecttype(rsp_evt)

                            self.logger.debug("Call is finished")

                    # whether it's scalar or a generator, if it raises an exception, serialize the exception as
                    # both the result and an event on the bus.
                    except Exception as e:
                        self.logger.exception(e)
                        rsp_evt = ExceptionEvent(
                            ns=e.__class__.__module__,
                            classname=e.__class__.__name__,
                            msg=str(e),
                            data=getattr(e, 'data', None),
                            code=getattr(e, 'code', '500'),
                            src_id=src_evt.id,
                            stacktrace=format_exc()
                        )
                        ret = dump_objecttype(rsp_evt)

        return ret

    def add_event_consumer(self, consumer_fn, *event_types, save_result_for_sync_mutation=True):
        """
        This is the same as add_event_consumer, but supports being used as a function decorator. See
        Microservice.event_consumer for complete documentation
        """

        is_generator = inspect.isgeneratorfunction(consumer_fn)
        for etype in event_types:
            if consumer_fn in {c[2] for c in self.event_consumers[etype]}:
                raise ValueError(f"Tried to add a consumer {consumer_fn.__name__} twice.")
            self.event_consumers[etype].append((is_generator, save_result_for_sync_mutation, consumer_fn))

    def event_consumer(self, *event_types, save_result_for_sync_mutation=True):
        """
        This is the same as add_event_consumer, but supports being used as a function decorator. See
        Microservice.event_consumer for complete documentation
        """

        def wrapped(consumer_fn):
            self.add_event_consumer(consumer_fn, *event_types,
                                    save_result_for_sync_mutation=save_result_for_sync_mutation)
            return consumer_fn

        return wrapped


class Microservice:
    """
    A microservice host object. Instantiate this object with a name and register all your services.

    Attributes:
        - logger (logging.Logger): The service system's logger
        - name (str): The service name. Should be identifier-like, as it is also the default topic name.
        - consumers (Dict[str, function]): A dict of all consumers that have been registered.
        - queries (Dict[str, g.ObjectType): A dict of all the queries associated with this service.
        - mutations (Dict[str, g.ObjectType): A dict of all the mutations associated with this service.
        - consumer_node (ConsumerNode): If this is running as a consumer, this will be defined as the current
            ConsumerNode object this consumer process is running as.

    Flask Config Variables:
        - KAFKA_BOOTSTRAP_SERVERS: ['localhost:9092']. The bootstrap servers for Kafka
        - RECENT_RESULTS_HOST: 'localhost'. The redis host for storing recent results for sync endpoints
        - RECENT_RESULTS_DB: 1. The redis db for storing recent results.
        - RECENT_RESULTS_PORT: 6379. The redis port for the recent results store.
        - RECENT_RESULTS_TTL: 60. The TTL for recent results
        - SVC_WEB_HOST: 'localhost'. The redis host for storing system status for each microservice.
        - SVC_WEB_PORT: 6379. The redis port for the system status host.
        - SVC_WEB_DB: 10. The redis db for storing system status.
    """
    _service_registry = {}
    _event_registry = {}

    def __init__(self, name: str):
        self.logger = get_task_logger(name)
        self.name = name
        self._registered_exceptions = {}
        self.consumers = ConsumerGroup(self)
        self.queries = {}
        self.mutations = {}
        self.types = []
        Microservice._service_registry[name] = self

    def register_type(self, t):
        self.types.append(t)

    def consumer_group(self, group_id, *topics_or_microservices):
        return self.consumers

    def raise_for_evt(self, evt):
        """
        Raises an exception if the event is an ExceptionEvent

        Args:
            evt (BaseEventMixin): An event to check
        """
        if isinstance(evt, ExceptionEvent):
            if not evt.ns or evt.ns in {'__builtin__', '__builtins__'}:
                self._registered_exceptions[evt.ns, evt.classname] = __builtins__[evt.classname]
            elif (evt.ns, evt.classname) not in self._registered_exceptions:
                self._registered_exceptions[evt.ns, evt.classname] = getattr(importlib.import_module(evt.ns), evt.classname)
            ex = self._registered_exceptions[evt.ns, evt.classname](evt.msg, **(evt.data or {}))
            raise ex

    def consumer_post_fork(self):
        """
        Override this method to do stuff AFTER the subprocess has forked.

        This method is highly useful to to things like initialize database resources, create connections to external
        resources that the consumer needs, etc.
        """

    def event_consumer(self, *event_types, topic=None, group_id=None, save_result_for_sync_mutation=True):
        """
        A decorator that wraps a function and turns it into a consumer.

        This is the main workhorse, other than the mutations. To use this decorator, write a function that can
        consume a single event as its sole positional parameter. The function can return None, return an Event
        (an ObjectType that incorporates the BaseEventMixin class), or it can `yield` events one at a time.

        If it returns none, it does not generate new events, and importantly it *cannot* be used to consume synchronous
        event mutations, as it will never report status to the mutation.

        If it returns an Event, then that event will be placed on the Kafka topic and also reported as a recent result
        on the Redis result broker.

        If it *yields* Events, then each event will be placed on the Kafka topic as it is yielded. Then the final
        yielded event will be consumed as if it was a returned event.

        Typically every mutation defined by a Microservice will have at least one event_consumer.

        Args:
            topic (optional str or tuple): The topic that the consumer should subscribe to. If this is a tuple, then
                multiple topics will be subscribed to.  If no topic is given, then the Microservice default topic, its
                name, will be the subscribed topic
            group_id (optional str): The consumer group that the consumer should report to Kafka. All consumers
                reporting the same consumer group share a cursor in Kafka. If omitted, this is the fully qualified
                function name.
            save_result_for_sync_mutation (bool): Default True. If this is set, then the return from the decorated
                function will be treated as the result object that goes in redis. You should have *exactly one*
                consumer with this set to true for any mutation where synchronous calling is allowed.
            *event_types (ObjectType): A list of ObjectType/BaseEventMixin classes that this consumer will
                respond to when they show up on the Kafka topic.


        Returns:
            The original function. The wrapped function is stored on the microservice itself.
        """

        def wrapper(fn):
            self.consumers.add_event_consumer(fn, *event_types, save_result_for_sync_mutation=save_result_for_sync_mutation)
            return fn
        return wrapper

    def init_app(self, app):
        """
        Initialize the microservice from a config.

        Args:
            app: A flask app or a dict

        Returns:

        """

        # note this is not a bound task. self is a closure over init_app
        @celery.task(ignore_result=True, name=f"{self.name}.consume_event_async")
        def call_service_async(event):
            self.consumers.consume_event(load_objecttype(event))

        # this is also not a bound task. self is bound to init_app::self
        @celery.task(name=f"{self.name}.consume_event_sync")
        def call_service_sync(event):
            return self.consumers.consume_event(load_objecttype(event))

        self.logger.info("Creating %s mutations classes", len(self.mutations))
        self.Mutations = type('Mutations', (g.ObjectType,), {m: self.mutations[m].Field() for m in self.mutations})


    def default_consumer_config(self, harakiri_limit=None, harakiri_jitter=None):
        return {}

