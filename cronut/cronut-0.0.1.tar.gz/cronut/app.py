#!/usr/bin/env python

__author__ = "Patrick Godwin (patrick.godwin@ligo.org)"
__description__ = "a module to store the application instance"

#-------------------------------------------------
### imports

import logging
import signal
import sys

from confluent_kafka import Consumer, KafkaError


#-------------------------------------------------
### classes

class App(object):
    """Implements a Kafka application for event processing.

    Parameters
    ----------
    name : `str`
        the name of the application instance
    broker :  `str`
        the Kafka broker to connect to
    process_cadence : `float`
        maximum rate at which data is processed, defaults to 0.1s
    num_messages : `int`
        max number of messages to process at once, defaults to 10
    timeout : `float`
        timeout for requesting messages from a topic, defaults to 0.2s

    """
    def __init__(self, name, broker, num_messages=10, timeout=0.2):
        self.name = name

        ### processing settings
        self.timeout = timeout
        self.num_messages = num_messages
        self.is_running = False

        ### kafka settings
        self._kafka_settings = {
            'bootstrap.servers': broker,
            'group.id': name
        }
        self._consumer = Consumer(self._kafka_settings)

        ### stateful/stateless processors
        self._processors = {}

        ### signal handler
        for sig in [signal.SIGINT, signal.SIGTERM]:
            signal.signal(sig, self._catch)


    def start(self):
        """Starts the application instance.

        """
        logging.info('starting {}...'.format(self.name.replace('_', ' ')))
        self._consumer.subscribe([topic for topic in self._processors.keys()])
        self.is_running = True
        self._run()


    def stop(self):
        """Stops the application instance.

        """
        logging.info('shutting down {}...'.format(self.name.replace('_', ' ')))
        self._fetch()
        self.is_running = False


    def stateful(self, topics, state=None):
        """Adds a stateful process for a given topic. Does the same
        thing as :meth:`add_stateful_process`, but is meant to be
        used as a decorator.

        Parameters
        ----------
        topics : `str` or `iterable`
            the name of the topic(s) to process
        state : `object`
            if specified, initial value for state

        """
        def wrapper(func):
            self.add_stateful_process(topics, func, state=state)
            return func
        return wrapper


    def add_stateful_process(self, topics, func, state=None):
        """Adds a stateful process for a given topic.

        Parameters
        ----------
        topics : `str` or `iterable`
            the name of the topic(s) to process
        func : `callable`
            the function to call when a message arrives
        state : `object`
            if specified, initial value for state
        """
        if isinstance(topics, str):
            topics = [topics]
        for topic in topics:
            if topic in self._processors:
                raise KeyError('topic already has a process defined for it')
            else:
                self._processors[topic] = {
                    'func': func,
                    'stateful': True,
                    'state': state
                }


    def stateless(self, topics):
        """Adds a stateless process for a given topic. Does the same
        thing as :meth:`add_stateless_process`, but is meant to be
        used as a decorator.

        Parameters
        ----------
        topics : `str` or `iterable`
            the name of the topic(s) to process

        """
        def wrapper(func):
            self.add_stateless_process(topics, func)
            return func
        return wrapper


    def add_stateless_process(self, topics, func):
        """Adds a stateless process for a given topic.

        Parameters
        ----------
        topicis : `str` or `iterable`
            the name of the topic to process
        func : `callable`
            the function to call when a message arrives
        """
        if isinstance(topics, str):
            topics = [topics]
        for topic in topics:
            if topic in self._processors:
                raise KeyError('topic already has a process defined for it')
            else:
                self._processors[topic] = {
                    'func': func,
                    'stateful': False
                }


    def _fetch(self):
        """Fetch messages from Kafka.

        """
        messages = self._consumer.consume(
            num_messages=self.num_messages,
            timeout=self.timeout
        )

        for message in messages:
            if message and not message.error():
                processor = self._processors[message.topic()]
                if processor['stateful']:
                    processor['func'](message, processor['state'])
                else:
                    processor['func'](message)


    def _run(self):
        """Processes events.

        """
        while self.is_running:
            self._fetch()


    def _catch(self, signum, frame):
        """Shuts down the application gracefully before exiting.

        """
        logging.info("SIG {:d} received, attempting graceful shutdown...".format(signum))
        self.stop()
        sys.exit(0)
