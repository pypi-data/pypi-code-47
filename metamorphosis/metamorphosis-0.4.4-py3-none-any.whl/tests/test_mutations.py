from contextlib import ExitStack

import msgpack
import pytest
from unittest import mock
from unittest.mock import patch

import graphene as g

from metamorphosis import EventMutation, MutationTimings, BaseEventMixin, Microservice
from metamorphosis.events import dump_objecttype


class Evt(g.ObjectType, BaseEventMixin):
    timing = g.Field(MutationTimings)
    string = g.String()


class CEvt(g.ObjectType):
    integer = g.Int()


@pytest.fixture
def ms():
    return Microservice('ms')


def test_async_mutation(ms):
    class AsyncMutation(EventMutation):
        microservice = ms
        mutation_event_type = Evt

        @classmethod
        def mutate_event(cls, root, info, **kwargs):
            return Evt(string=kwargs['a_string'])

    with patch.object(ms, 'producer') as ms_producer:
        root = 1
        info = 2

        rsp = AsyncMutation.mutate(root, info, a_string="A String")
        ms_producer.send.assert_called()
        ms_producer.flush.assert_called()
        assert isinstance(rsp, AsyncMutation)
        assert isinstance(rsp.data, Evt)
        assert rsp.data.string == 'A String'


def test_sync_mutation(ms):
    class SyncMutation(EventMutation):
        microservice = ms
        mutation_event_type = Evt
        allowed_timings = (MutationTimings.synchronous, MutationTimings.asynchronous)
        default_timing = MutationTimings.synchronous
        consequent_objecttypes = (CEvt,)

        class Arguments:
            timing = g.Argument(MutationTimings, default_value=MutationTimings.asynchronous)

        @classmethod
        def mutate_event(cls, root, info, **kwargs):
            return Evt(string=kwargs['a_string'], timing=kwargs.get('timing', cls.default_timing))

    with ExitStack() as stack:
        producer = stack.enter_context(patch.object(ms, 'producer'))
        raise_for_evt = stack.enter_context(patch.object(ms, 'raise_for_evt'))
        recent_results = stack.enter_context(patch.object(ms, 'recent_results'))
        ms.recent_results.exists = mock.Mock(side_effect=[False, True])
        ms.recent_results.get = mock.Mock(side_effect=[msgpack.packb(dump_objecttype(CEvt(integer=20)))])
        mock_time = stack.enter_context(patch('metamorphosis.mutations.time'))

        rsp = SyncMutation.mutate(None, None, a_string='A String')
        producer.send.assert_called()
        producer.flush.assert_called()
        raise_for_evt.assert_called()
        mock_time.sleep.assert_called_with(SyncMutation.polling_delta)

        assert isinstance(rsp, SyncMutation)
        assert isinstance(rsp.data, CEvt)

