"""
# The definition of the Microservice host object
"""
import importlib
import inspect
import logging
from collections import defaultdict
from os import getpid
from traceback import format_exc
from typing import TypeVar

import graphene as g
import msgpack
from flask import current_app
from kafka import KafkaProducer, KafkaConsumer
from redis import StrictRedis

from metamorphosis.events import ExceptionEvent, dump_objecttype, load_objecttype
from metamorphosis.service_web import (
    StopMicroservice, StopConsumer, StopNode,
    StopConsumerProcess, ConsumerProcessFinished)

E = TypeVar('E', bound=Exception)


class ConsumerGroup:
    """
    A group of consumer functions that are run inside of a single process.

    Do not create this directly. Instead create these objects through Microservice().consumer_group(...)
    or the @microservice.event_consumer() decorator.
    """

    def __init__(self, microservice, group_id, topics_or_microservices):
        self.microservice = microservice
        self.event_consumers = defaultdict(list)
        self.topics = [t.name if isinstance(t, Microservice) else t for t in topics_or_microservices]
        self.group_id = group_id
        self.logger = microservice.logger.getChild(self.group_id)

    def create_consumer(self):
        topics_to_subscribe_to = (self.microservice.consumer_node.service_web_topic, *self.topics)

        # create our consumer and attach it to the current mainloop
        consumer = KafkaConsumer(
            *topics_to_subscribe_to,
            bootstrap_servers=self.microservice.bootstrap_servers,
            group_id=self.group_id)

        self.logger.info("Consumer setup listening on topics %s with group_id %s", topics_to_subscribe_to,
                         self.group_id)

        return consumer

    def __call__(self, harakiri_limit=None):
        """This is the callable that gets run as the consumer process"""
        pid = getpid()
        node_name = self.microservice.consumer_node.node_name
        proc_name = f'{node_name}:{self.microservice.name}:{self.group_id}:{pid}'
        service_store_pids_key = f'metamorphosis.consumers:{self.microservice.name}.{self.group_id}:pids'

        # add this consumer's pid to the list of pids under management
        self.logger.info("Consumer %s:%s process set name to %s", self.microservice.name, self.group_id, proc_name)
        self.microservice.service_status_store.sadd(service_store_pids_key, proc_name)

        consumer = self.create_consumer()

        # Consume messages
        self.logger.info('Consumer-process %s post-fork routine running if any', proc_name)
        self.microservice.consumer_post_fork()
        self.logger.info('Consumer-process %s set up and starting', proc_name)
        n_messages_consumed = 0
        for msg in consumer:
            # deserialize the data into a json-like structure
            evt_data = msgpack.unpackb(msg.value, raw=False)
            # use that structure to populate g.ObjectTypes, in this case a CreateForm event.
            src_evt = load_objecttype(evt_data)
            self.logger.info(f"Received event {src_evt}")

            # if the event is one of the stop signals, then quit.
            if self.microservice.should_i_stop(src_evt, self.group_id):
                self.logger.info("Consumer %s for service %s on node %s finished all events. Exiting now.",
                                 self.group_id, self.microservice.name, self.microservice.consumer_node.node_name)

                # let the bus know we're quitting
                self.microservice.send_event(self.microservice.service_web_topic, ConsumerProcessFinished(
                    node=self.microservice.consumer_node.node_name,
                    pid=pid,
                    name=self.group_id,
                    reason=src_evt.__class__.__name__,
                    exit_code='0'
                ))
                consumer.commit()
                self.microservice.service_status_store.srem(service_store_pids_key, proc_name)
                return True

            # if the event is one the consumer is listening for, process it.
            else:
                self._consume_event(src_evt)

                # we've consumed a message, so increment the number consumed by 1, then...
                n_messages_consumed += 1

                # check if we've reached our limit for this process. If we have, exit gracefully
                if harakiri_limit and n_messages_consumed >= harakiri_limit:
                    self.logger.info('Harakiri limit reached upon finishing the last event. Exiting.')
                    self.microservice.send_event(current_app.config['SVC_WEB_TOPIC'], ConsumerProcessFinished(
                        node=self.microservice.consumer_node.node_name,
                        pid=pid,
                        name=self.group_id,
                        reason='Harakiri',
                        exit_code='0'
                    ))
                    consumer.commit()
                    self.microservice.service_status_store.srem(service_store_pids_key, proc_name)
                    return True

    def _consume_event(self, src_evt):
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
                                    self.microservice.recent_results.setex(
                                        # add that to the recent results for sync mutations
                                        str(src_evt.id),
                                        self.microservice.recent_results_ttl,
                                        msgpack.packb(dump_objecttype(rsp_evt))
                                    )
                                self.logger.debug("Sending event to %s, %s", t, rsp_evt)
                                self.microservice.send_event(t,
                                                             rsp_evt)  # and send it on the bus for any async listeners
                                self.logger.debug("Call is finished.")
                        else:  # otherwise, every yielded object should be an event
                            rsp_evt = None
                            for rsp_evt in fn(src_evt):  # for each yielded object,
                                if isinstance(rsp_evt, tuple):
                                    t, rsp_evt = rsp_evt
                                else:
                                    t = self.microservice.name
                                self.logger.debug("Sending event to %s, %s", t, rsp_evt)
                                self.microservice.send_event(t, rsp_evt)  # send it on the bus, but it's not a "result"

                            if save_result_for_sync_mutation:
                                self.microservice.recent_results.setex(  # treat the last event yielded as a result
                                    str(src_evt.id),
                                    self.microservice.recent_results_ttl,
                                    msgpack.packb(dump_objecttype(rsp_evt))
                                )
                            self.logger.debug("Call is finished")

                    # whether it's scalar or a generator, if it raises an exception, serialize the exception as
                    # both the result and an event on the bus.
                    except Exception as e:
                        self.logger.error(e)
                        rsp_evt = ExceptionEvent(
                            ns=e.__class__.__module__,
                            classname=e.__class__.__name__,
                            msg=str(e),
                            data=getattr(e, 'data', None),
                            code=getattr(e, 'code', '500'),
                            src_id=src_evt.id,
                            stacktrace=format_exc()
                        )

                        self.microservice.recent_results.setex(
                            src_evt.id,
                            self.microservice.recent_results_ttl,
                            msgpack.packb(dump_objecttype(rsp_evt))
                        )

                        self.microservice.send_event(self.microservice.name, rsp_evt)

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
    _event_registry = {}

    RECENT_RESULTS_HOST = 'RECENT_RESULTS_HOST'
    RECENT_RESULTS_PORT = 'RECENT_RESULTS_PORT'
    RECENT_RESULTS_DB = 'RECENT_RESULTS_DB'
    RECENT_RESULTS_TTL = 'RECENT_RESULTS_TTL'
    KAFKA_BOOTSTRAP_SERVERS = 'KAFKA_BOOTSTRAP_SERVERS'
    SVC_WEB_HOST = 'SVC_WEB_HOST'
    SVC_WEB_PORT = 'SVC_WEB_PORT'
    SVC_WEB_DB = 'SVC_WEB_DB'
    SVC_WEB_TOPIC = 'SVC_WEB_TOPIC'
    config_defaults = {
        KAFKA_BOOTSTRAP_SERVERS: ['localhost:9092'],
        RECENT_RESULTS_HOST: 'localhost',
        RECENT_RESULTS_DB: 1,
        RECENT_RESULTS_PORT: 6379,
        RECENT_RESULTS_TTL: 60,
        SVC_WEB_HOST: 'localhost',
        SVC_WEB_PORT: 6379,
        SVC_WEB_DB: 10,
        SVC_WEB_TOPIC: 'metamorphosis.services'
    }

    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.name = name
        self._registered_exceptions = {}
        self.consumers = {}
        self.queries = {}
        self.mutations = {}
        self.producer = None
        self.consumer_node = None
        self.recent_results = None
        self.recent_results_ttl = 60
        self.service_web_topic = 'metamorphosis.services'
        self.types = []

    def register_type(self, t):
        self.types.append(t)

    def consumer_group(self, group_id, *topics_or_microservices):
        if not topics_or_microservices:
            topics_or_microservices = [self]
        cg = ConsumerGroup(self, group_id, topics_or_microservices)
        self.consumers[group_id] = cg
        return cg

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

    def should_i_stop(self, evt, consumer_name):
        """
        Checks to see if any stop events relate to a given consumer.

        Args:
            evt: A StopMicroservice, StopConsumer, StopNode, or StopConsumerProcess event
            consumer_name: The consumer name to check against

        Returns:
            True if this consumer process should stop in response to the event. False if not.
        """
        if isinstance(evt, StopMicroservice) and evt.name == self.name:
            self.logger.info("Got microservice shutdown signal for %s. Stopping cleanly.", self.name)
            return True
        elif isinstance(evt, StopConsumer) and evt.name == consumer_name:
            self.logger.info("Got consumer shutdown signal for %s. Stopping cleanly.", consumer_name)
            return True
        elif isinstance(evt, StopNode) and evt.name == self.consumer_node.node_name:
            self.logger.info("Got node shutdown signal for %s. Stopping cleanly.", self.consumer_node.node_name)
            return True
        elif (
            isinstance(evt, StopConsumerProcess) and
            evt.name == consumer_name and
            evt.node == self.consumer_node.node_name and
            evt.pid == getpid()
        ):
            self.logger.info("this consumer process %s:%s:%s got the signal to finish up.",
                             evt.node, evt.name, evt.pid)
            return True
        else:
            return False

    def send_event(self, topic, evt):
        """Serialize and send an ObjectType that is also a BaseEventMixin to a given topic"""
        self.producer.send(topic, msgpack.packb(dump_objecttype(evt)))

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
            if fn.__name__ in self.consumers:
                raise KeyError(f"{fn.__name__} already exists in consumers. Pick a unique function name")

            g = ConsumerGroup(
                self,
                group_id if group_id else fn.__name__,
                [topic] if topic else [self.name],
            )
            g.add_event_consumer(fn, *event_types, save_result_for_sync_mutation=save_result_for_sync_mutation)
            self.consumers[fn.__name__] = g
            return fn
        return wrapper

    def init_app(self, app):
        """
        Initialize the microservice from a config.

        Args:
            app: A flask app or a dict

        Returns:

        """
        config = getattr(app, 'config', app)  # either this is a flask app, which will have a config, or this is a dict
        self.service_web_topic = config.get(self.SVC_WEB_TOPIC)

        self.recent_results = StrictRedis(
            host=config.get(self.RECENT_RESULTS_HOST, self.config_defaults[self.RECENT_RESULTS_HOST]),
            port=config.get(self.RECENT_RESULTS_PORT, self.config_defaults[self.RECENT_RESULTS_PORT]),
            db=config.get(self.RECENT_RESULTS_DB, self.config_defaults[self.RECENT_RESULTS_DB])
        )
        self.recent_results_ttl = config.get(self.RECENT_RESULTS_TTL,
                                             self.config_defaults[self.RECENT_RESULTS_TTL])  # seconds ttl for redis
        self.bootstrap_servers = config.get(self.KAFKA_BOOTSTRAP_SERVERS,
                                            self.config_defaults[self.KAFKA_BOOTSTRAP_SERVERS])
        self.service_status_store = StrictRedis(
            host=config.get(self.SVC_WEB_HOST, self.config_defaults[self.SVC_WEB_HOST]),
            port=config.get(self.SVC_WEB_PORT, self.config_defaults[self.SVC_WEB_PORT]),
            db=config.get(self.SVC_WEB_DB, self.config_defaults[self.SVC_WEB_DB]),
        )
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)

        self.logger.info("Creating %s mutations classes", len(self.mutations))
        self.Mutations = type('Mutations', (g.ObjectType,), {m: self.mutations[m].Field() for m in self.mutations})

    def default_consumer_config(self, harakiri_limit=None, harakiri_jitter=None):
        return {
            self.name: {
                consumer: {
                    "procs": 1,
                    "harakiri_limit": harakiri_limit,
                    "harakiri_jitter": harakiri_jitter
                } for consumer in self.consumers
            }
        }


