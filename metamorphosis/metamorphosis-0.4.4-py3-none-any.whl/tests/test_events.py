import datetime
import enum

import graphene as g
import pytest
from unittest import mock

from metamorphosis.events import dump_objecttype, load_objecttype


class TEnum(g.Enum):
    A = 0
    B = 1
    C = 2


class Simple(g.ObjectType):
    tint = g.Int()
    tstring = g.String()
    tjson = g.JSONString()
    tdatetime = g.DateTime()
    tdate = g.Date()
    ttime = g.Time()
    tboolean = g.Boolean()
    tenum = g.Field(TEnum)

    def __eq__(self, other):
        return all((getattr(self, field) == getattr(other, field) for field in self.__class__._meta.fields))


class Nested(g.ObjectType):
    data = g.Field(Simple)


class UnionTest(g.Union):
    class Meta:
        types = (Simple, Nested)


@pytest.mark.parametrize(
    'test_object,expected',
    [
        (Simple(),{}),
        (Simple(tint=1),{}),
        (Simple(tenum=TEnum.A),{}),
        (Simple(tjson={'a': [1,2,3]}),{}),
        (Simple(tint=1, tstring="asdf"),{}),
        (Simple(tdate=datetime.date.today()),{}),
        (Simple(tdatetime=datetime.datetime.now()),{}),
        (Simple(ttime=datetime.time(12,4,0,0)),{}),
        (Nested(data=Simple(tint=1)),{}),
        (UnionTest(Simple(tint=2)),{}),
    ]
)
def test_objecttype_serialization(test_object, expected):
    frozen = dump_objecttype(test_object)

    assert hasattr(frozen, 'keys')
    assert '_type' in frozen
    assert frozen['_type'] == test_object.__class__.__name__
    assert '_ns' in frozen
    assert frozen['_ns'] == test_object.__class__.__module__
    if hasattr(test_object.__class__._meta, 'fields'):
        for field in test_object.__class__._meta.fields:
            if getattr(test_object, field) is not None:
                assert field in frozen

    thawed = load_objecttype(frozen)
    assert thawed.__class__.__name__ == test_object.__class__.__name__
    if hasattr(test_object.__class__._meta, 'fields'):
        for field in test_object.__class__._meta.fields:
            assert getattr(test_object, field) == getattr(thawed, field)

