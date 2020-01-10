import uuid

from xbus import xbus_pb2

from . import checksum


class EnvelopeWriter:
    def __init__(self, send, event_types):
        self.envelope = xbus_pb2.Envelope()
        env_id = uuid.uuid4()
        self.envelope.id = env_id.bytes
        self.envelope.eventIDs[:] = [uuid.uuid4().bytes for _ in event_types]
        self.event_types = event_types
        self.event_checksums = {
            et: checksum.Checksum(evID + et.encode("ascii"))
            for evID, et in zip(self.envelope.eventIDs, event_types)
        }

        self.send = send

        self.item_queues = {et: list() for et in event_types}

    async def add_items(self, event_type, *items):
        for item in items:
            self.event_checksums[event_type].update(item)
        self.item_queues[event_type].extend(items)

    async def close(self):
        for id, event_type in zip(self.envelope.eventIDs, self.event_types):
            event = self.envelope.events.add()
            event.id = id
            event.type = event_type
            event.index = 1
            event.itemCount = len(self.item_queues[event_type])
            event.checksum = self.event_checksums[event_type].final()
            event.items[:] = self.item_queues[event_type]
        await self.send(self.envelope)
