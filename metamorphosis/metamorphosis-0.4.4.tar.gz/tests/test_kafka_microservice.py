from collections import namedtuple
from contextlib import ExitStack
from unittest.mock import patch

import msgpack
import pytest
import graphene as g

from metamorphosis import Microservice, BaseEventMixin, StopMicroservice, StopConsumer, StopNode, StopConsumerProcess
from metamorphosis.events import ExceptionEvent, dump_objecttype


@pytest.fixture
def ms():
    return Microservice('ms')


class RegularEvt(g.ObjectType, BaseEventMixin):
    pass


def test_raise_for_evt(ms):
    ms.raise_for_evt(RegularEvt)
    with pytest.raises(Exception):
        ms.raise_for_evt(ExceptionEvent(classname="Exception", msg="A message"))

    with pytest.raises(KeyError):
        ms.raise_for_evt(ExceptionEvent(classname="KeyError", ns='__builtin__', msg="A message"))


def test_should_i_stop(ms):
    assert not ms.should_i_stop(RegularEvt(), 'anyconsumer')

    assert not ms.should_i_stop(StopMicroservice(name='otherms'), 'anyconsumer')
    assert ms.should_i_stop(StopMicroservice(name='ms'), 'anyconsumer')

    assert not ms.should_i_stop(StopConsumer(name='otherconsumer'), 'anyconsumer')
    assert ms.should_i_stop(StopConsumer(name='anyconsumer'), 'anyconsumer')

    with patch.object(ms, 'consumer_node', node_name='mynode'):
        assert not ms.should_i_stop(StopNode(name='othernode'), 'anyconsumer')
        assert ms.should_i_stop(StopNode(name='mynode'), 'anyconsumer')

        with patch('metamorphosis.microservice.getpid', side_effect=lambda: 10):
            assert not ms.should_i_stop(StopConsumerProcess(name='anyconsumer', node='mynode', pid=12), 'anyconsumer')
            assert not ms.should_i_stop(StopConsumerProcess(name='other', node='mynode', pid=10), 'any')
            assert not ms.should_i_stop(StopConsumerProcess(name='any', node='othernode', pid=10), 'any')
            assert ms.should_i_stop(StopConsumerProcess(name='anyconsumer', node='mynode', pid=10), 'anyconsumer')


def test_send_event(ms):
    with patch.object(ms, 'producer'):
        evt = RegularEvt(id='acef0117')
        ms.send_event('foo', evt)
        ms.producer.send.assert_called_with('foo', msgpack.packb(dump_objecttype(evt)))


App = namedtuple('Flask', ['config'])


def test_init_app_default(ms):
    default_config_app = App(config={})

    with ExitStack() as stack:
        sr = stack.enter_context(patch('metamorphosis.microservice.StrictRedis'))
        kc = stack.enter_context(patch('metamorphosis.microservice.KafkaConsumer'))
        kp = stack.enter_context(patch('metamorphosis.microservice.KafkaProducer'))
        ms.init_app(default_config_app)
        assert issubclass(ms.Mutations, g.ObjectType)
        assert ms.producer is not None
        assert ms.recent_results is not None


def test_init_app_custom(ms):
    custom_config_app = App(config={
        'RECENT_RESULTS_HOST': 'RECENT_RESULTS_HOST',
        'RECENT_RESULTS_PORT': 'RECENT_RESULTS_PORT',
        'RECENT_RESULTS_DB': 'RECENT_RESULTS_DB',
        'RECENT_RESULTS_TTL': 'RECENT_RESULTS_TTL',
        'KAFKA_BOOTSTRAP_SERVERS': 'KAFKA_BOOTSTRAP_SERVERS',
        'SVC_WEB_HOST': 'SVC_WEB_HOST',
        'SVC_WEB_PORT': 'SVC_WEB_PORT',
        'SVC_WEB_DB': 'SVC_WEB_DB',
    })

    with ExitStack() as stack:
        sr = stack.enter_context(patch('metamorphosis.microservice.StrictRedis'))
        kc = stack.enter_context(patch('metamorphosis.microservice.KafkaConsumer'))
        kp = stack.enter_context(patch('metamorphosis.microservice.KafkaProducer'))
        ms.init_app(custom_config_app)
        assert ms.recent_results_ttl == custom_config_app.config['RECENT_RESULTS_TTL']
        assert ms.bootstrap_servers == custom_config_app.config['KAFKA_BOOTSTRAP_SERVERS']
        sr.assert_called_with(
            host=custom_config_app.config['SVC_WEB_HOST'],
            port=custom_config_app.config['SVC_WEB_PORT'],
            db=custom_config_app.config['SVC_WEB_DB'],
        )

def test_event_consumer(ms):
    with patch('metamorphosis.microservice.ConsumerGroup') as cg:
        @ms.event_consumer(RegularEvt)
        def regular_evt_consumer(evt):
            pass

        assert 'regular_evt_consumer' in ms.consumers
        cg.assert_called_with(
            ms,
            'regular_evt_consumer',
            [ms.name],
        )
        ms.consumers['regular_evt_consumer'].add_event_consumer.assert_called_with(
            regular_evt_consumer, RegularEvt, save_result_for_sync_mutation=True)


        @ms.event_consumer(RegularEvt, topic='othertopic')
        def topic_evt_consumer(evt):
            pass

        assert 'topic_evt_consumer' in ms.consumers
        cg.assert_called_with(
            ms,
            'topic_evt_consumer',
            ['othertopic']
        )


        @ms.event_consumer(RegularEvt, group_id="other_group")
        def group_evt_consumer(evt):
            pass

        assert 'topic_evt_consumer' in ms.consumers
        cg.assert_called_with(
            ms,
            'other_group',
            ['ms']
        )

        @ms.event_consumer(RegularEvt, save_result_for_sync_mutation=False)
        def save_evt_consumer(evt):
            pass

        assert 'save_evt_consumer' in ms.consumers
        ms.consumers['save_evt_consumer'].add_event_consumer.assert_called_with(
            save_evt_consumer, RegularEvt, save_result_for_sync_mutation=False)

