import io
import json
from csv import DictWriter as Writer
from dataclasses import fields
from typing import Any, List, Optional, Type, Union

from .core import T
from .de import Deserializer as De
from .de import from_dict
from .se import Serializer as Se
from .se import asdict


class CsvSerializer(Se):
    writer: Writer

    @classmethod
    def serialize(cls, obj: Union[T, List[T]], header: bool = False, **opts) -> Optional[io.StringIO]:
        if not obj:
            return None

        buf = io.StringIO()
        if isinstance(obj, list):
            head = obj[0]
            objs = obj
        else:
            head = obj
            objs = [obj]
        writer = Writer(buf, [f.name for f in fields(head)])

        if header:
            writer.writeheader()
        for obj in objs:
            writer.writerow(asdict(obj))
        buf.seek(0)
        return buf


class CsvDeserializer(De):
    @classmethod
    def deserialize(cls, s, **opts):
        return json.loads(s, **opts)


def to_csv(obj: Any, se: Type[Se] = CsvSerializer, **opts) -> str:
    res = se.serialize(obj, **opts)
    if res:
        return res.read().rstrip() or ''
    else:
        return ''


def from_csv(c: Type[T], s: str, de: Type[De] = CsvDeserializer, **opts) -> T:
    return from_dict(c, de.deserialize(s, **opts))
