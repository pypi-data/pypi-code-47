from collections import namedtuple
from contextlib import ExitStack

import msgpack
import pytest
from unittest import mock
from unittest.mock import patch, Mock

import graphene as g
from metamorphosis import Microservice, BaseEventMixin, StopMicroservice
from metamorphosis.events import dump_objecttype


class RegularEvt(g.ObjectType, BaseEventMixin):
    pass


class SecondaryEvt(g.ObjectType, BaseEventMixin):
    pass


class TertiaryEvt(g.ObjectType, BaseEventMixin):
    pass


@pytest.fixture
def ms():
    return Microservice('ms')


@pytest.fixture
def grp(ms):
    return ms.consumer_group('ms_group', ms)


def test_add_event_consumer(grp):
    def fn_a(evt):
        pass

    def fn_b(evt):
        pass

    def generator_fn(evt):
        yield SecondaryEvt()
        return SecondaryEvt()

    grp.add_event_consumer(fn_a, RegularEvt)
    assert RegularEvt in grp.event_consumers
    assert (False, True, fn_a) in grp.event_consumers[RegularEvt]

    with pytest.raises(ValueError):
        grp.add_event_consumer(fn_a, RegularEvt)

    grp.add_event_consumer(fn_b, RegularEvt, SecondaryEvt)
    assert RegularEvt in grp.event_consumers
    assert SecondaryEvt in grp.event_consumers
    assert (False, True, fn_a) in grp.event_consumers[RegularEvt]
    assert (False, True, fn_b) in grp.event_consumers[RegularEvt]
    assert (False, True, fn_b) in grp.event_consumers[SecondaryEvt]

    grp.add_event_consumer(generator_fn, RegularEvt, save_result_for_sync_mutation=False)
    assert (True, False, generator_fn) in grp.event_consumers[RegularEvt]


def test_event_consumer_decorator(grp):
    with patch.object(grp, 'add_event_consumer'):
        @grp.event_consumer(RegularEvt, SecondaryEvt)
        def fn_a(evt):
            pass

        grp.add_event_consumer.assert_called_with(
            fn_a, RegularEvt, SecondaryEvt, save_result_for_sync_mutation=True)


def test_consume_event(ms, grp):
    with ExitStack() as stack:
        recent_results = stack.enter_context(patch.object(ms, 'recent_results'))
        producer = stack.enter_context(patch.object(ms, 'producer'))
        ExceptionEvent = stack.enter_context(patch('metamorphosis.microservice.ExceptionEvent'))
        a = Mock()
        b = Mock()
        c = Mock()

        def fn_a(evt):
            a()
            raise ValueError("Fake Error")

        def fn_b(evt):
            b()

        def generator_fn(evt):
            c()
            yield TertiaryEvt()
            return TertiaryEvt()

        grp.add_event_consumer(fn_a, RegularEvt)
        grp.add_event_consumer(fn_b, RegularEvt)
        grp.add_event_consumer(generator_fn, SecondaryEvt, save_result_for_sync_mutation=False)

        grp._consume_event(TertiaryEvt())
        a.assert_not_called()
        b.assert_not_called()
        c.assert_not_called()

        grp._consume_event(SecondaryEvt())
        a.assert_not_called()
        b.assert_not_called()
        c.assert_called()
        producer.send.assert_called()
        recent_results.setex.assert_not_called()

        grp._consume_event(RegularEvt())
        a.assert_called()
        b.assert_called()
        ExceptionEvent.assert_called()
        recent_results.setex.assert_called()


@pytest.mark.parametrize('events', [[TertiaryEvt(), SecondaryEvt(), RegularEvt(), StopMicroservice(name='ms')]])
def test_call(ms, grp, events):
    fake_msg = namedtuple('fake_msg',  'value')

    class FakeConsumer:
        def __init__(self, *evts):
            self.evts = evts

        def __iter__(self):
            return iter(self.evts)

        def commit(self):
            pass

    with ExitStack() as stack:
        evts = FakeConsumer(*[fake_msg(value=msgpack.packb(dump_objecttype(e))) for e in events])
        stack.enter_context(patch('metamorphosis.microservice.StrictRedis'))
        stack.enter_context(patch('metamorphosis.microservice.KafkaConsumer'))
        stack.enter_context(patch('metamorphosis.microservice.KafkaProducer'))
        App = namedtuple('Flask', ['config'])
        default_config_app = App(config={})
        ms.init_app(default_config_app)

        evts.commit = lambda: None

        stack.enter_context(patch('metamorphosis.microservice.getpid', side_effect=[10]))
        stack.enter_context(patch.object(ms, "consumer_node"))
        sss = stack.enter_context(patch.object(ms, "service_status_store"))
        stack.enter_context(patch.object(grp, 'create_consumer', side_effect=[evts]))
        consumer_post_fork = stack.enter_context(patch.object(ms, 'consumer_post_fork'))
        stack.enter_context(patch.object(ms, 'recent_results'))
        stack.enter_context(patch.object(ms, 'producer'))
        stack.enter_context(patch('metamorphosis.microservice.ExceptionEvent'))

        a = Mock()
        b = Mock()
        c = Mock()

        def fn_a(evt):
            a()
            raise ValueError("Fake Error")

        def fn_b(evt):
            b()

        def generator_fn(evt):
            c()
            yield TertiaryEvt()
            return TertiaryEvt()

        grp.add_event_consumer(fn_a, RegularEvt)
        grp.add_event_consumer(fn_b, RegularEvt)
        grp.add_event_consumer(generator_fn, SecondaryEvt, save_result_for_sync_mutation=False)

        grp()
        consumer_post_fork.assert_called()
        a.assert_called()
        b.assert_called()
        c.assert_called()
        sss.srem.assert_called()






